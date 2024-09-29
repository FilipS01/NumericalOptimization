# line_search_factory.py
from LineSearch.armijo import ArmijoSearch
from LineSearch.goldstein import GoldsteinSearch
from LineSearch.wolfe import WolfeSearch


class LineSearchFactory:
    @staticmethod
    def create_line_search(line_search_type):
        if line_search_type == "Armijo":
            return ArmijoSearch()
        elif line_search_type == "Goldstein":
            return GoldsteinSearch()
        elif line_search_type == "Wolfe":
            return WolfeSearch()
        else:
            raise ValueError(f"Unknown Line Search method: {line_search_type}")