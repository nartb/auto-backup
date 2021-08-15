from time import sleep

from helper import click_elements_containing_strings, wait_until_num_files_downloaded, SLEEP_TIME


def download_todoist_backup(driver, credentials, download_dir):
    # Get login page
    driver.get("https://todoist.com/users/showlogin")
    sleep(SLEEP_TIME)

    # Populate credentials
    driver.find_element_by_id('email').send_keys(credentials['todoist']['username'])
    driver.find_element_by_id('password').send_keys(credentials['todoist']['password'])
    sleep(SLEEP_TIME)

    # Click login button
    driver.find_elements_by_css_selector("#login_form button")[0].click()
    sleep(SLEEP_TIME)

    # Downlad most recent backup
    driver.get("https://todoist.com/app/settings/backups")
    sleep(SLEEP_TIME)
    driver.find_elements_by_css_selector(".no-focus-marker ul a")[0].click()

    # Wait until 1 file downloaded
    wait_until_num_files_downloaded(download_dir, 1)



def download_notion_backup(driver, credentials, download_dir):
    # Get login page
    driver.get("https://www.notion.so/login")
    sleep(SLEEP_TIME)

    # Populate email
    driver.find_element_by_id('notion-email-input-1').send_keys(credentials['notion']['username'])
    sleep(SLEEP_TIME)

    # Click to continue
    driver.find_elements_by_css_selector('form .notion-focusable')[1].click()
    sleep(SLEEP_TIME)

    # Populate password
    driver.find_element_by_id('notion-password-input-2').send_keys(credentials['notion']['password'])
    sleep(SLEEP_TIME)

    # Click to continue
    driver.find_elements_by_css_selector('form .notion-focusable')[1].click()
    sleep(SLEEP_TIME)

    # Navigate to export button and click
    click_elements_containing_strings(driver, [
        'Settings & Members',
        'Settings',
        'Export all workspace content',
        'Markdown & CSV',
        'HTML',
        'Export'
    ])

    # Wait until 1 file downloaded
    wait_until_num_files_downloaded(download_dir, 1)


BACKUP_FUNCTION_DICT = {
    'todoist': download_todoist_backup,
    'notion': download_notion_backup
}