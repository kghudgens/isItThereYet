from scraper import Scraper
from data import FormatData


def main():
    scraper = Scraper()
    scraper.company_selector()
    scraper.close_driver()

    dataFormatter = FormatData(scraper.unstructured_data, {})
    dataFormatter.prep_data()
    dataFormatter.create_results_file()


if __name__ == "__main__":
    main()
