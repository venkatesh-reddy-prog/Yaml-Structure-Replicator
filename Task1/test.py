from util import *
if __name__ == '__main__':
    src_folder = 'bic'
    dest_folder = 'destination_folder'
    updates = {'national': "abcd", 'martin': {'job': 'DevOps'}, 'appname': 'done', 'type': 'prod'}
 
    main(src_folder, dest_folder, updates)