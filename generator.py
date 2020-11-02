import requests
import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path
from requests.exceptions import ConnectionError

class Generator:

    def __init__(self):
        url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
        try:
            self._requests = requests.get(url)
        except ConnectionError:
            self._requests = None
            print(
                "It was not possible to load data from the repositories on GitHub.\n"+
                "Please check your internet connection and try again."
            )

    def _generate_image(self, file_name, x_values, y_values, bar_width, title):
        plt.rcParams['figure.figsize'] = (30, 30)
        plt.xticks(rotation=90)
        plt.yticks(np.arange(y_values[-1], y_values[0], 5000))
        plt.bar(x_values, y_values, color = "green", width = bar_width)
        plt.suptitle(title)
        plt.savefig(file_name.with_suffix('.png'), format ='png', dpi = 300)
        plt.savefig(file_name.with_suffix('.svg'), format ='svg',dpi = 300)
        plt.close()

    def generate_chart(self):
        content = self._requests.json()
        items = content["items"]
        names_values = []
        names = []
        values = []

        for item in items:
            names_values.append((item["name"], item["stargazers_count"]))

        # Sorted by stargazers_count in descending order.
        names_values.sort(key=lambda x: x[1], reverse=True)

        for name, value in names_values:
            names.append(name)
            values.append(value)

        home = Path.home()
        directory = home / 'data'
        directory.mkdir(exist_ok=True)

        self._generate_image(directory / 'Popularity Repositories', names, values, 0.1, 'Popularity Repositories')
        self._generate_image(directory / 'Six Most Popular Repositories', names[:6], values[:6], 0.6, 'Six Most Popular Repositories')
