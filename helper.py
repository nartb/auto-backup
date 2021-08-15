from time import sleep
import os
import shutil

SLEEP_TIME = 3


def click_element_containing_string(driver, string_to_click):
    driver.find_elements_by_xpath(f'//*[text() = "{string_to_click}"]')[0].click()


def click_elements_containing_strings(driver, strings_to_click):
    for string_to_click in strings_to_click:
        click_element_containing_string(driver, string_to_click)
        sleep(SLEEP_TIME)
        

def wait_until_num_files_downloaded(download_dir, num_expected):
    num_downloaded = 0
    
    # Continue until expected number of of files reached
    while num_downloaded < num_expected:
        print(f'Waiting... Downloaded {num_downloaded} of {num_expected}')
        sleep(SLEEP_TIME)
        
        # Update number of files downloaded
        num_downloaded = len([f for f in os.listdir(download_dir) if not f.endswith('.crdownload')])

    print('Done!')


def download_backups(backups_to_download, backups_dir, backup_function_dict, driver, credentials):
    for backup in backups_to_download:
        # Create directory to store backup
        backup_dir = os.path.join(backups_dir, backup)
        os.mkdir(backup_dir)
        
        # Define download directory
        download_dir = os.path.join(backups_dir, 'download')

        # Call function to download backup
        backup_function_dict[backup](driver, credentials, download_dir)

        # Move files out of download dir
        move_downloaded_files_to_backup_dir(download_dir, backup_dir)


def move_downloaded_files_to_backup_dir(download_dir, backup_dir):
    # Get files to move
    files = os.listdir(download_dir)

    # Move files one by one
    for file in files:
        shutil.move(os.path.join(download_dir, file), backup_dir)