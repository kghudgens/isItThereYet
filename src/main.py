from scraper import Scraper
from data import FormatData
from email_sender import SendEmail


def main():
    scraper = Scraper()
    scraper.company_selector()
    scraper.close_driver()

    dataFormatter = FormatData(scraper.unstructured_data, {})
    dataFormatter.prep_data()
    dataFormatter.create_results_file()

    sender = SendEmail()
    sender.create_email_content()


if __name__ == "__main__":
    main()
