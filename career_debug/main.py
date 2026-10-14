from commands import CustomParser

def run_cli():
    cp = CustomParser()
    cp.initiate_parse()
    cp.add_career_parser()
    cp.add_notes_parser()
    cp.add_questions_parser()

    args = cp.parser.parse_args()

    if args.command == "career":
        if args.career_action == "notes":
            print(args.notes)
        elif args.career_action == "questions":
            print(args.questions)

if __name__ == "__main__":
    run_cli()
