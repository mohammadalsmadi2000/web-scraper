import requests
from bs4 import BeautifulSoup

class WikipediaScraper:
    def __init__(self):
        pass

    def get_citations_needed_count(self, url):
        """
        Count the number of citations needed on a Wikipedia page.

        Args:
            url (str): The URL of the Wikipedia page.

        Returns:
            int: The number of citations needed.

        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        citations = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
        return len(citations)

    def get_citations_needed_report(self, url):
        """
        Generate a report of citations needed on a Wikipedia page.

        Args:
            url (str): The URL of the Wikipedia page.

        Returns:
            str: The report string with each citation listed.

        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        citations = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
        report = ""
        for citation in citations:
            passage = citation.find_parent("p").text.strip()
            report += f"{passage}\n\n"
        return report

    def create_report_file(self, url, filename="citations_report.md"):
        """
        Create a text file with the citations report.

        Args:
            url (str): The URL of the Wikipedia page.
            filename (str): The name of the file to be created.

        """
        report = self.get_citations_needed_report(url)
        styled_report = f"# Citations Report\n\n{report}"
        with open(filename, "w") as file:
            file.write(styled_report)
        print(f"Citations report has been saved to {filename}.")

if __name__=="__main__":

    #Example
    scraper = WikipediaScraper()
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    count = scraper.get_citations_needed_count(URL)
    print(f"Number of citations needed: {count}")

    report = scraper.get_citations_needed_report(URL)
    print("Citations needed report:")
    print(report)

    scraper.create_report_file(URL)