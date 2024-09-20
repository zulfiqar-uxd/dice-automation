
# Dice Job Apply Automation Script

This project automates the process of fetching job links from Dice, cleaning the job link data, and applying for jobs. The automation is divided into three scripts:

1. **`fetch_job_links.py`**: Fetches job listings from Dice based on keywords.
2. **`clean.py`**: Removes duplicate job links from the fetched list.
3. **`apply_to_jobs.py`**: Automatically applies to jobs from the cleaned list.

## Prerequisites

1. **Python 3.x**: Ensure Python is installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

2. **Google Chrome**: The automation uses Selenium WebDriver to control Google Chrome. Ensure you have the latest version of Chrome installed. You can download Chrome from [here](https://www.google.com/chrome/).

3. **ChromeDriver**: The ChromeDriver must match the version of your installed Chrome browser. You can download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

4. **Selenium**: Install Selenium for Python using the following command:
   ```bash
   pip install selenium
   ```

## Setup

### 1. Check Chrome Version and Download ChromeDriver

Before running the automation, check your Chrome browser version:

1. Open Chrome and navigate to `chrome://settings/help`.
2. Take note of the Chrome version.

Now, download the correct version of **ChromeDriver** from the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads), and place it in your project directory.

### 2. Update Keywords in `fetch_job_links.py`

By default, the script fetches jobs using a set of pre-defined keywords. You can customize these keywords as needed:

1. Open `fetch_job_links.py`.
2. Modify the `self.query_list` array to include your desired job search keywords:
   ```python
   self.query_list = ['ux ', 'ui ', 'ui/ ', 'ux/ ', 'user experience', 'visual design']
   ```

### 3. Run the Scripts in Sequence

#### Step 1: Fetch Job Links

To fetch job listings from Dice based on the specified keywords, run the `fetch_job_links.py` script:

```bash
python fetch_job_links.py
```

This script will save the fetched job links to a file named `new_id.txt`.

#### Step 2: Clean the Job Links

After fetching the job links, run the `clean.py` script to remove duplicates and create a clean list of unique job links:

```bash
python clean.py
```

This will output the cleaned links to a file named `cleaned.txt`.

#### Step 3: Apply to Jobs

Finally, run the `apply_to_jobs.py` script to apply for the jobs from the cleaned list:

1. Open `apply_to_jobs.py`.
2. Update the `email` and `password` fields with your Dice account credentials:
   ```python
   email = "your_email"
   password = "your_password"
   ```
3. Run the script:
   ```bash
   python apply_to_jobs.py
   ```

The script will read job links from `cleaned.txt` and attempt to apply to the jobs.

## Detailed Steps

1. **Download ChromeDriver**:
   - Check your Chrome version and download the matching ChromeDriver version.
   - Place the ChromeDriver in the project directory and update the path in both `fetch_job_links.py` and `apply_to_jobs.py` if necessary.

2. **Run the Job Fetcher**:
   - Open a terminal or command prompt.
   - Run `fetch_job_links.py` to scrape job listings from Dice based on the keywords you set in the script.
   - The job links will be stored in `new_id.txt`.

3. **Clean the Job Links**:
   - After fetching, run `clean.py` to remove duplicate job links from the list.
   - The cleaned links will be saved in `cleaned.txt`.

4. **Apply to Jobs**:
   - Run `apply_to_jobs.py` to automatically apply for jobs using your Dice credentials.
   - Make sure you have updated your login credentials in the script before running it.

## Notes

- **Chrome Options**: The scripts are designed to run Chrome in full-screen mode, but you can run them in headless mode by uncommenting the following line in both `fetch_job_links.py` and `apply_to_jobs.py`:
   ```python
   # chrome_options.add_argument("--headless")
   ```
   Headless mode allows Chrome to run without opening a browser window, which can be useful for running scripts on servers or in the background.

- **Logging**: Each script outputs relevant progress information to the console, such as the number of jobs fetched, cleaned, and applied to.

- **Error Handling**: If the script encounters issues during job application, it will log the error and skip to the next job.

## Conclusion

This automation saves you time by fetching, cleaning, and applying to jobs on Dice with minimal manual input. Customize the search keywords, and let the script do the work for you!

Feel free to contribute or improve the automation by submitting pull requests or issues on the GitHub repository.
