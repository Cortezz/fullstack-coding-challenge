import threading
import time

from app.services import unbabel_api
from app.models import post, translation

def perform():
    print "Starting Unbabel polling job"
    translations = translation.get_by_not_status('completed')
    unfinished_translations = []

    start_time = time.time()
    threads = [threading.Thread(target=update_translation,
        args=(t, unfinished_translations)) for t in translations
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    if len(unfinished_translations) == 0:
        print "No unfinished translations!"
    print("Polling completed: it took %s seconds ---" % (time.time() - start_time))

def update_translation(trans, unfinished_translations):
    machine_translation = unbabel_api.get_mt_translation(trans['uid'])
    if machine_translation['status'] == 'completed':
        trans['status'] = 'completed'
        trans['translated_text'] = machine_translation['translated_text']
        translation.update(trans)
        p = post.get(trans['post_id'])
        p['title_%s'%trans['target_language']] = machine_translation['translated_text']
        post.update(p)
    else:
        unfinished_translations.append(translation['uid'])
