{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMJPGxTM1nMBz7845UNN+Ra",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jeanbouteiller-ds/tennis_prediction/blob/main/test.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 245
        },
        "id": "X79ndvP7Ga2_",
        "outputId": "75d7f1b7-ba6a-42c1-b172-db1e1dff35d8"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-16-c3579983c4dd>\u001b[0m in \u001b[0;36m<cell line: 10>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mfile_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'tennis_prediction/test_data.txt'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfile_path\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'w'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mfile\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mitem\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mlist_test\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m         \u001b[0mfile\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"%s\\n\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mitem\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'tennis_prediction/test_data.txt'"
          ]
        }
      ],
      "source": [
        "# import pickle\n",
        "import datetime\n",
        "import os\n",
        "\n",
        "list_test = [datetime.datetime.now()]\n",
        "\n",
        "# Specify the file path within the data folder in the GitHub workspace\n",
        "file_path = 'test_data.txt'\n",
        "\n",
        "with open(file_path, 'a') as file:\n",
        "    for item in list_test:\n",
        "        file.write(str(item) + \"\\n\")\n",
        "\n",
        "# print(list_test)\n"
      ]
    }
  ]
}