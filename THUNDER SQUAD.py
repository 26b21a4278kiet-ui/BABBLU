{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNzmq55REA6lx3+eYQIz7sW",
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
        "<a href=\"https://colab.research.google.com/github/26b21a4278kiet-ui/BABBLU/blob/main/THUNDER%20SQUAD.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EMD2yqW5hNSW",
        "outputId": "eb5e9ff9-0465-4812-af3a-cd5f767a2820",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=======================================================\n",
            "Sports Team Rating System\n",
            "=======================================================\n",
            "Benchmark Dataset : Custom College Football Benchmark\n",
            "Number of Teams   : 5\n",
            "Number of Matches : 10\n",
            "=======================================================\n"
          ]
        }
      ],
      "source": [
        "# ============================================================\n",
        "# TEAM HEADER & CUSTOM BENCHMARK DATASET\n",
        "# ============================================================\n",
        "\n",
        "project_title = \"Sports Team Rating System\"\n",
        "dataset_name = \"Custom College Football Benchmark\"\n",
        "\n",
        "teams = [\"Team A\", \"Team B\", \"Team C\", \"Team D\", \"Team E\"]\n",
        "\n",
        "# Point-differential match results\n",
        "# A beat B by 5, B beat C by 3, etc.\n",
        "matches = [\n",
        "    (\"Team A\", \"Team B\", 5),\n",
        "    (\"Team B\", \"Team C\", 3),\n",
        "    (\"Team C\", \"Team D\", 4),\n",
        "    (\"Team D\", \"Team E\", 2),\n",
        "    (\"Team E\", \"Team A\", 1),\n",
        "    (\"Team A\", \"Team C\", 6),\n",
        "    (\"Team B\", \"Team D\", 3),\n",
        "    (\"Team C\", \"Team E\", 5),\n",
        "    (\"Team D\", \"Team A\", 2),\n",
        "    (\"Team E\", \"Team B\", 4)\n",
        "]\n",
        "\n",
        "print(\"=\" * 55)\n",
        "print(project_title)\n",
        "print(\"=\" * 55)\n",
        "print(\"Benchmark Dataset :\", dataset_name)\n",
        "print(\"Number of Teams   :\", len(teams))\n",
        "print(\"Number of Matches :\", len(matches))\n",
        "print(\"=\" * 55)"
      ]
    }
  ]
}