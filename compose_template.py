# import os
# import re
import string
import random

from graph_template import Graph, Vertex


def get_words_from_text(text_path: str) -> list[str]:
    with open(text_path, "r") as f:
        text = f.read()

        # turn whitespace into just spaces
        # example: "      hello       world     ".split()
        # returns: ["hello", "world"]

        text = " ".join(text.split())

        # working with all lowercase chars is easier
        text = text.lower()

        # now we could be complex and deal with punctuation but there are cases where you might add
        # a period such as Mr. Brightside but that's not really punctuation... so we just remove
        # all the punctuation.
        # hello! it's me. --> hello its me

        text = text.translate(str.maketrans("", "", string.punctuation))

    # split on spaces again and return
    return text.split()


def make_graph(words: list[str]) -> Graph:
    graph = Graph()
    prev_word: Vertex | None = None

    for word in words:
        # check that word is in graph, if not -> add it
        vertex = graph.get_vertex(word)

        # if there was a previous word, then add an edge if it does not already exist
        # in the graph, otherwise increment weight by 1

        if prev_word:
            prev_word.increment_edge(vertex)

        # set our word to the previous word and iterate
        prev_word = vertex

    # we want to generate the probability mappings before composing.
    # this is a great place to do it before we return the graph object
    graph.generate_probability_mappings()
    return graph


def compose(graph: Graph, words: list[str], length=50) -> list[str]:
    composition: list[str] = []

    # pick random word to start
    word = graph.get_vertex(random.choice(words))

    for _ in range(length):
        composition.append(word.value)
        word = graph.get_next_word(word)

    return composition


def main() -> None:
    # get words from text
    words = get_words_from_text("texts/hp_sorcerer_stone.txt")

    # make graph using those words
    graph = make_graph(words)

    # get the next word for x number of words (defined by user)

    # show the user
    composition = compose(graph, words, 100)

    # returns string where all words are separated by space
    print(" ".join(composition))


if __name__ == "__main__":
    main()
