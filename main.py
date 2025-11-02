#!/usr/bin/env python3
"""
Text Analysis & Humanizer - Main Application
A comprehensive tool for bias detection, AI text humanization, and text formatting.

Features:
- Bias detection in writing
- AI text humanization
- Multiple format support (MLA, Essay, Letter, Cover Letter, Resume)
- Word counting and analysis
- Comparison to high-quality standards
"""

import sys
import argparse
from typing import Optional

from bias_detector import BiasDetector, format_bias_report
from ai_humanizer import AIHumanizer, format_ai_analysis_report
from text_formatter import TextFormatter
from text_analyzer import TextAnalyzer, format_analysis_report


class TextProcessingApp:
    def __init__(self):
        """Initialize the application with all components."""
        self.bias_detector = BiasDetector()
        self.ai_humanizer = AIHumanizer()
        self.text_formatter = TextFormatter()
        self.text_analyzer = TextAnalyzer()

    def process_text(self, text: str, options: dict) -> dict:
        """
        Process text based on specified options.

        Args:
            text: The input text to process
            options: Dictionary of processing options

        Returns:
            Dictionary with all results
        """
        results = {
            'original_text': text,
            'processed_text': text,
            'analyses': {}
        }

        # Step 1: Analyze for bias (if requested)
        if options.get('detect_bias', False):
            print("\n[1/5] Detecting bias...")
            bias_results = self.bias_detector.detect_bias(text)
            results['analyses']['bias'] = bias_results

        # Step 2: Analyze AI likelihood (if requested)
        if options.get('analyze_ai', False):
            print("\n[2/5] Analyzing AI likelihood...")
            ai_analysis = self.ai_humanizer.analyze_ai_likelihood(text)
            results['analyses']['ai_detection'] = ai_analysis

        # Step 3: Humanize text (if requested)
        if options.get('humanize', False):
            print("\n[3/5] Humanizing text...")
            results['processed_text'] = self.ai_humanizer.humanize_text(
                results['processed_text']
            )

        # Step 4: Format text (if format specified)
        if options.get('format_type'):
            print(f"\n[4/5] Formatting text as {options['format_type']}...")
            format_params = options.get('format_params', {})
            results['processed_text'] = self.text_formatter.format_text(
                results['processed_text'],
                options['format_type'],
                **format_params
            )

        # Step 5: Analyze text statistics (always done)
        print("\n[5/5] Analyzing text statistics...")
        text_type = options.get('format_type', 'essay')
        if text_type not in ['essay', 'cover_letter', 'resume', 'letter']:
            text_type = 'essay'

        analysis = self.text_analyzer.analyze_text(
            results['processed_text'],
            text_type
        )
        results['analyses']['statistics'] = analysis

        return results

    def generate_report(self, results: dict, options: dict) -> str:
        """
        Generate a comprehensive report from the processing results.

        Args:
            results: Processing results dictionary
            options: Processing options used

        Returns:
            Formatted report string
        """
        report_sections = []

        # Header
        report_sections.append("=" * 80)
        report_sections.append("TEXT PROCESSING REPORT".center(80))
        report_sections.append("=" * 80)

        # Bias Detection Report
        if 'bias' in results['analyses']:
            report_sections.append("\n" + "=" * 80)
            report_sections.append("BIAS DETECTION")
            report_sections.append("=" * 80)
            report_sections.append(format_bias_report(results['analyses']['bias']))

        # AI Detection Report
        if 'ai_detection' in results['analyses']:
            report_sections.append("\n" + "=" * 80)
            report_sections.append("AI TEXT ANALYSIS")
            report_sections.append("=" * 80)
            report_sections.append(format_ai_analysis_report(results['analyses']['ai_detection']))

        # Text Statistics Report
        if 'statistics' in results['analyses']:
            report_sections.append("\n" + "=" * 80)
            report_sections.append("TEXT STATISTICS & QUALITY")
            report_sections.append("=" * 80)
            report_sections.append(format_analysis_report(results['analyses']['statistics']))

        # Processed Text (if different from original)
        if results['processed_text'] != results['original_text']:
            report_sections.append("\n" + "=" * 80)
            report_sections.append("PROCESSED TEXT")
            report_sections.append("=" * 80)
            report_sections.append("\n" + results['processed_text'])
            report_sections.append("\n" + "=" * 80)

        return "\n".join(report_sections)


def interactive_mode():
    """Run the application in interactive mode."""
    print("=" * 80)
    print("Welcome to Text Analysis & Humanizer".center(80))
    print("=" * 80)
    print("\nThis tool helps you:")
    print("  1. Detect bias in your writing")
    print("  2. Humanize AI-generated text")
    print("  3. Format text in various styles (MLA, Essay, Letter, etc.)")
    print("  4. Analyze text statistics and quality")
    print("\n" + "=" * 80)

    app = TextProcessingApp()

    # Get text input
    print("\n📝 STEP 1: INPUT TEXT")
    print("-" * 80)
    print("Enter or paste your text (press Ctrl+D or Ctrl+Z when done):")
    print("-" * 80)

    try:
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break
        text = "\n".join(lines)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
        return

    if not text.strip():
        print("\n❌ Error: No text provided.")
        return

    # Get processing options
    print("\n\n🔧 STEP 2: SELECT OPTIONS")
    print("-" * 80)

    options = {}

    # Bias detection
    response = input("Detect bias? (y/n): ").strip().lower()
    options['detect_bias'] = response == 'y'

    # AI detection
    response = input("Analyze AI likelihood? (y/n): ").strip().lower()
    options['analyze_ai'] = response == 'y'

    # Humanize
    response = input("Humanize text (remove AI markers)? (y/n): ").strip().lower()
    options['humanize'] = response == 'y'

    # Format
    response = input("Format text? (y/n): ").strip().lower()
    if response == 'y':
        print("\nAvailable formats:")
        print("  1. MLA (academic paper)")
        print("  2. Essay")
        print("  3. Letter")
        print("  4. Cover Letter")
        print("  5. Resume")
        print("  6. Plain (basic cleanup)")

        format_choice = input("Choose format (1-6): ").strip()
        format_map = {
            '1': 'mla',
            '2': 'essay',
            '3': 'letter',
            '4': 'cover_letter',
            '5': 'resume',
            '6': 'plain'
        }

        if format_choice in format_map:
            options['format_type'] = format_map[format_choice]

            # Get format-specific parameters
            print(f"\nOptional parameters for {options['format_type']} format:")
            print("(Press Enter to skip any parameter)")

            format_params = {}

            if options['format_type'] == 'mla':
                format_params['author'] = input("  Author name: ").strip() or None
                format_params['title'] = input("  Paper title: ").strip() or None
                format_params['instructor'] = input("  Instructor name: ").strip() or None
                format_params['course'] = input("  Course name: ").strip() or None

            elif options['format_type'] == 'essay':
                format_params['title'] = input("  Essay title: ").strip() or None
                format_params['author'] = input("  Author name: ").strip() or None

            elif options['format_type'] in ['letter', 'cover_letter']:
                format_params['your_name'] = input("  Your name: ").strip() or None
                format_params['recipient_name'] = input("  Recipient name: ").strip() or None

                if options['format_type'] == 'cover_letter':
                    format_params['position'] = input("  Position applying for: ").strip() or None
                    format_params['company_name'] = input("  Company name: ").strip() or None

            elif options['format_type'] == 'resume':
                format_params['name'] = input("  Your name: ").strip() or None
                format_params['contact'] = input("  Contact info: ").strip() or None

            # Clean up None values
            format_params = {k: v for k, v in format_params.items() if v}
            options['format_params'] = format_params

    # Process text
    print("\n\n⚙️  PROCESSING...")
    print("-" * 80)

    try:
        results = app.process_text(text, options)
        report = app.generate_report(results, options)

        print("\n\n" + "=" * 80)
        print("RESULTS")
        print("=" * 80)
        print(report)

        # Save option
        print("\n\n💾 SAVE RESULTS")
        print("-" * 80)
        response = input("Save results to file? (y/n): ").strip().lower()
        if response == 'y':
            filename = input("Enter filename (default: results.txt): ").strip()
            if not filename:
                filename = "results.txt"

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)

            print(f"✓ Results saved to {filename}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description='Text Analysis & Humanizer - Comprehensive text processing tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python main.py

  # Process file with all features
  python main.py -f input.txt -b -a -h -t essay -o output.txt

  # Just detect bias
  python main.py -f input.txt -b

  # Humanize and format as cover letter
  python main.py -f input.txt -h -t cover_letter
        """
    )

    parser.add_argument(
        '-f', '--file',
        help='Input file path',
        type=str
    )

    parser.add_argument(
        '-b', '--bias',
        help='Detect bias in text',
        action='store_true'
    )

    parser.add_argument(
        '-a', '--ai-analysis',
        help='Analyze AI likelihood',
        action='store_true'
    )

    parser.add_argument(
        '-h', '--humanize',
        help='Humanize AI text',
        action='store_true',
        dest='humanize_flag'
    )

    parser.add_argument(
        '-t', '--format-type',
        help='Format type (mla, essay, letter, cover_letter, resume, plain)',
        type=str,
        choices=['mla', 'essay', 'letter', 'cover_letter', 'resume', 'plain']
    )

    parser.add_argument(
        '-o', '--output',
        help='Output file path',
        type=str
    )

    args = parser.parse_args()

    # If no file specified, run interactive mode
    if not args.file:
        interactive_mode()
        return

    # Read input file
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Process text
    app = TextProcessingApp()

    options = {
        'detect_bias': args.bias,
        'analyze_ai': args.ai_analysis,
        'humanize': args.humanize_flag,
        'format_type': args.format_type,
        'format_params': {}
    }

    try:
        results = app.process_text(text, options)
        report = app.generate_report(results, options)

        # Output results
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Results saved to {args.output}")
        else:
            print(report)

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
