#!/usr/bin/env python3
"""
Example usage of the Text Analysis & Humanizer modules.
Demonstrates all features with sample text.
"""

from bias_detector import BiasDetector, format_bias_report
from ai_humanizer import AIHumanizer, format_ai_analysis_report
from text_formatter import TextFormatter
from text_analyzer import TextAnalyzer, format_analysis_report


def example_1_bias_detection():
    """Example: Detect bias in text"""
    print("\n" + "=" * 80)
    print("EXAMPLE 1: BIAS DETECTION")
    print("=" * 80)

    text = """
    The chairman called the meeting to order. He discussed how mankind has made
    significant progress in technology. The lady doctor presented her findings,
    while the male nurse assisted. We need young blood to bring fresh perspectives
    to the organization. The candidate seems articulate and well-spoken for his
    background.
    """

    detector = BiasDetector()
    results = detector.detect_bias(text)
    print(format_bias_report(results))


def example_2_ai_humanization():
    """Example: Humanize AI-generated text"""
    print("\n" + "=" * 80)
    print("EXAMPLE 2: AI TEXT HUMANIZATION")
    print("=" * 80)

    ai_text = """
    As an AI language model, I would like to inform you that it is important to note
    that climate change is a significant issue. Furthermore, it is essential to
    understand that we must take action. Moreover, it should be noted that numerous
    studies have been conducted. In conclusion, we must endeavor to facilitate
    positive change in order to achieve our objectives.
    """

    print("\nORIGINAL TEXT:")
    print("-" * 80)
    print(ai_text)

    humanizer = AIHumanizer()

    # Analyze AI likelihood
    analysis = humanizer.analyze_ai_likelihood(ai_text)
    print("\n" + format_ai_analysis_report(analysis))

    # Humanize the text
    humanized = humanizer.humanize_text(ai_text)

    print("\nHUMANIZED TEXT:")
    print("-" * 80)
    print(humanized)


def example_3_text_formatting():
    """Example: Format text in different styles"""
    print("\n" + "=" * 80)
    print("EXAMPLE 3: TEXT FORMATTING")
    print("=" * 80)

    text = """
    Artificial intelligence has transformed the way we work and live. Machine
    learning algorithms can now process vast amounts of data in seconds. This
    technology is being applied across industries from healthcare to finance.

    The impact of AI extends beyond automation. It's changing how we make decisions
    and solve complex problems. However, we must also consider the ethical
    implications of these powerful tools.

    As we move forward, it's crucial to develop AI responsibly and ensure it
    benefits all of humanity.
    """

    formatter = TextFormatter()

    # Example 3a: MLA Format
    print("\n3A. MLA FORMAT:")
    print("-" * 80)
    mla_formatted = formatter.format_text(
        text,
        'mla',
        author='John Smith',
        instructor='Dr. Jane Doe',
        course='Computer Science 101',
        title='The Impact of Artificial Intelligence on Society'
    )
    print(mla_formatted)

    # Example 3b: Cover Letter Format
    print("\n\n3B. COVER LETTER FORMAT:")
    print("-" * 80)
    cover_letter_text = """
    I am writing to express my strong interest in the Software Engineer position
    at your company. With five years of experience in full-stack development and
    a passion for creating innovative solutions, I believe I would be an excellent
    addition to your team.

    In my current role at Tech Corp, I have led the development of several
    successful projects that improved system efficiency by 40%. I specialize in
    Python, JavaScript, and cloud technologies, which align perfectly with your
    job requirements.

    I am excited about the opportunity to contribute to your mission of building
    cutting-edge software solutions. Thank you for considering my application.
    """

    cover_letter_formatted = formatter.format_text(
        cover_letter_text,
        'cover_letter',
        your_name='Jane Developer',
        your_email='jane@email.com',
        your_phone='(555) 123-4567',
        company_name='TechCorp Inc.',
        position='Senior Software Engineer',
        hiring_manager='Mr. Robert Johnson'
    )
    print(cover_letter_formatted)


def example_4_text_analysis():
    """Example: Analyze text statistics and quality"""
    print("\n" + "=" * 80)
    print("EXAMPLE 4: TEXT ANALYSIS & STATISTICS")
    print("=" * 80)

    text = """
    Climate change represents one of the most pressing challenges of our time.
    Rising global temperatures are causing significant environmental disruptions.
    These include melting polar ice caps, rising sea levels, and more frequent
    extreme weather events.

    The scientific consensus is clear: human activities, particularly the burning
    of fossil fuels, are the primary driver of recent climate change. Carbon
    dioxide and other greenhouse gases trap heat in the atmosphere, creating a
    warming effect.

    Addressing this crisis requires immediate action at multiple levels. Governments
    must implement strong environmental policies. Businesses need to adopt sustainable
    practices. Individuals can make a difference through conscious choices in their
    daily lives.

    The transition to renewable energy sources like solar and wind power is essential.
    So is improving energy efficiency in buildings and transportation. We must also
    protect and restore forests, which absorb carbon dioxide from the atmosphere.

    While the challenge is daunting, solutions exist. By working together and taking
    decisive action now, we can mitigate the worst effects of climate change and
    create a sustainable future for generations to come.
    """

    analyzer = TextAnalyzer()
    analysis = analyzer.analyze_text(text, text_type='essay')
    print(format_analysis_report(analysis))


def example_5_complete_workflow():
    """Example: Complete workflow combining all features"""
    print("\n" + "=" * 80)
    print("EXAMPLE 5: COMPLETE WORKFLOW")
    print("=" * 80)

    ai_generated_text = """
    As an AI language model, I would like to discuss the benefits of remote work.
    It is important to note that remote work has become increasingly popular.
    Furthermore, numerous studies have shown that it can increase productivity.
    Moreover, it is worth noting that employees often report better work-life balance.
    However, it should be noted that challenges exist. In conclusion, organizations
    must carefully consider their approach to remote work in order to maximize
    benefits while minimizing drawbacks.
    """

    print("\nSTEP 1: ORIGINAL TEXT")
    print("-" * 80)
    print(ai_generated_text)

    # Step 1: Detect bias
    print("\n\nSTEP 2: BIAS DETECTION")
    print("-" * 80)
    detector = BiasDetector()
    bias_results = detector.detect_bias(ai_generated_text)
    print(f"Bias Score: {bias_results['overall_bias_score']:.2f}/100")
    print(f"Inclusivity Score: {bias_results['inclusivity_score']:.2f}/100")

    # Step 2: Analyze AI likelihood
    print("\n\nSTEP 3: AI DETECTION")
    print("-" * 80)
    humanizer = AIHumanizer()
    ai_analysis = humanizer.analyze_ai_likelihood(ai_generated_text)
    print(f"AI Probability: {ai_analysis['ai_probability']:.1f}/100")
    print(f"Assessment: {ai_analysis['assessment']}")

    # Step 3: Humanize
    print("\n\nSTEP 4: HUMANIZING TEXT")
    print("-" * 80)
    humanized = humanizer.humanize_text(ai_generated_text)
    print(humanized)

    # Step 4: Format
    print("\n\nSTEP 5: FORMATTING AS ESSAY")
    print("-" * 80)
    formatter = TextFormatter()
    formatted = formatter.format_text(
        humanized,
        'essay',
        title='The Benefits of Remote Work',
        author='Sarah Johnson'
    )
    print(formatted)

    # Step 5: Analyze final text
    print("\n\nSTEP 6: FINAL ANALYSIS")
    print("-" * 80)
    analyzer = TextAnalyzer()
    final_analysis = analyzer.analyze_text(formatted, text_type='essay')
    print(f"Word Count: {final_analysis['word_count']}")
    print(f"Quality Score: {final_analysis['quality_score']['score']}/100")
    print(f"Assessment: {final_analysis['quality_score']['assessment']}")
    print(f"Reading Level: {final_analysis['reading_level']}")


def main():
    """Run all examples"""
    print("\n" + "=" * 80)
    print("TEXT ANALYSIS & HUMANIZER - EXAMPLES")
    print("=" * 80)
    print("\nThis script demonstrates all features of the text processing system.")
    print("Each example showcases different capabilities.\n")

    try:
        example_1_bias_detection()
        input("\n\nPress Enter to continue to next example...")

        example_2_ai_humanization()
        input("\n\nPress Enter to continue to next example...")

        example_3_text_formatting()
        input("\n\nPress Enter to continue to next example...")

        example_4_text_analysis()
        input("\n\nPress Enter to continue to next example...")

        example_5_complete_workflow()

        print("\n\n" + "=" * 80)
        print("ALL EXAMPLES COMPLETED!")
        print("=" * 80)
        print("\nTo use the interactive application, run: python main.py")
        print("For command-line usage, run: python main.py --help")

    except KeyboardInterrupt:
        print("\n\nExamples interrupted by user.")
    except Exception as e:
        print(f"\n\nError running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
