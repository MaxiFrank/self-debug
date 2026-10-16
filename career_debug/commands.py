import argparse
# from Typing import List
import sys

# TODO: check is it camelcase??
class CustomParser:
    def __init__(self):
        self.parser = None
        self.career_subparsers = None
        self.notes_parser = None
        self.questions_parser = None

    def initiate_parse(self):
        # TODO: Add docstring and type checking
        self.parser = argparse.ArgumentParser()

    def add_career_parser(self):
        parser = self.parser

        subparsers = self.parser.add_subparsers(dest="command", required=True)
        career_parser = subparsers.add_parser("career")
        
        career_subparsers = career_parser.add_subparsers(dest="career_action")
        self.career_subparsers = career_subparsers
    
    def add_notes_parser(self):
        notes_parser = self.career_subparsers.add_parser("notes")
        
        
        notes_parser.add_argument("notes", help="Add career notes")
        self.notes_parser = notes_parser

    def add_questions_parser(self):
        questions_parser = self.career_subparsers.add_parser("questions")
        questions_parser.add_argument("questions", help="Add career questions")
        self.questions_parser = questions_parser
