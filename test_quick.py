#!/usr/bin/env python3
"""
Quick test to verify all modules work correctly.
"""

def test_bias_detector():
    from bias_detector import BiasDetector
    detector = BiasDetector()
    text = "The chairman discussed the issue."
    results = detector.detect_bias(text)
    assert 'overall_bias_score' in results
    assert 'gender_bias' in results
    print("✓ Bias Detector: PASS")

def test_ai_humanizer():
    from ai_humanizer import AIHumanizer
    humanizer = AIHumanizer()
    text = "As an AI language model, I would like to inform you."
    humanized = humanizer.humanize_text(text)
    assert len(humanized) > 0
    assert "As an AI language model" not in humanized
    print("✓ AI Humanizer: PASS")

def test_text_formatter():
    from text_formatter import TextFormatter
    formatter = TextFormatter()
    text = "This is a test."
    formatted = formatter.format_text(text, 'plain')
    assert len(formatted) > 0
    print("✓ Text Formatter: PASS")

def test_text_analyzer():
    from text_analyzer import TextAnalyzer
    analyzer = TextAnalyzer()
    text = "This is a test. It has multiple sentences. We can analyze it."
    analysis = analyzer.analyze_text(text)
    assert 'word_count' in analysis
    assert analysis['word_count'] > 0
    print("✓ Text Analyzer: PASS")

def test_main_app():
    from main import TextProcessingApp
    app = TextProcessingApp()
    text = "This is a test."
    options = {'detect_bias': True, 'humanize': False}
    results = app.process_text(text, options)
    assert 'processed_text' in results
    assert 'analyses' in results
    print("✓ Main App: PASS")

if __name__ == '__main__':
    print("Running quick tests...\n")
    try:
        test_bias_detector()
        test_ai_humanizer()
        test_text_formatter()
        test_text_analyzer()
        test_main_app()
        print("\n" + "=" * 50)
        print("ALL TESTS PASSED! ✓")
        print("=" * 50)
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
