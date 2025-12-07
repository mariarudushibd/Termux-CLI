"""Main CLI entry point"""

import argparse
import sys
from pathlib import Path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog='termux-cli',
        description='A local coding agent for your terminal'
    )
    parser.add_argument(
        '--dir', '-d',
        type=str,
        default='.',
        help='Working directory for the agent'
    )
    parser.add_argument(
        '--model', '-m',
        type=str,
        default='claude-3-sonnet',
        help='AI model to use'
    )
    parser.add_argument(
        '--config', '-c',
        type=str,
        help='Path to config file'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    from .repl import REPL
    repl = REPL(working_dir=args.dir, model=args.model)
    repl.run()

if __name__ == '__main__':
    main()
