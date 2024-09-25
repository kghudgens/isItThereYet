import datetime


class FormatData:

    def __init__(self, unstructured_data, structured_data):
        self.unstructured_data = unstructured_data
        self.structured_data = structured_data

    def prep_data(self):
        req_count = 0
        for k, v in self.unstructured_data.items():
            for i in v:
                if "Engineer" in i or "Developer" in i:
                    req_count += 1
                    self.structured_data[k + "-" + str(req_count)] = i

    def create_results_file(self):
        with open("isItThere.txt", "w") as file:
            file.write("Current Time : " + str(datetime.datetime.now()) + "\n")
            file.write(
                "Amount of hits returned : " + str(len(self.structured_data)) + "\n"
            )

            print("\n")
            for k, v in self.structured_data.items():
                file.write(k + "\n")
                file.write(v + "\n\n")

            file.close()
