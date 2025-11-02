"""
Text Analyzer Module
Provides word counting, statistics, and comparison to high-quality standards.
"""

import re
import math
from typing import Dict, List, Tuple
from collections import Counter


class TextAnalyzer:
    def __init__(self):
        """Initialize the text analyzer with standard benchmarks."""
        # Reading level benchmarks (Flesch-Kincaid grade level)
        self.reading_level_standards = {
            'elementary': (0, 5),
            'middle_school': (6, 8),
            'high_school': (9, 12),
            'college': (13, 16),
            'graduate': (17, float('inf'))
        }

        # Quality benchmarks for different text types
        self.quality_standards = {
            'essay': {
                'min_words': 300,
                'ideal_words': (500, 1500),
                'max_words': 3000,
                'avg_sentence_length': (15, 20),
                'vocabulary_diversity': 0.5,  # Unique words / total words
                'paragraph_count': (3, 10)
            },
            'cover_letter': {
                'min_words': 200,
                'ideal_words': (250, 400),
                'max_words': 500,
                'avg_sentence_length': (12, 18),
                'vocabulary_diversity': 0.55,
                'paragraph_count': (3, 5)
            },
            'resume': {
                'min_words': 200,
                'ideal_words': (300, 600),
                'max_words': 800,
                'avg_sentence_length': (10, 15),
                'vocabulary_diversity': 0.6,
                'paragraph_count': (4, 8)
            },
            'letter': {
                'min_words': 150,
                'ideal_words': (200, 500),
                'max_words': 750,
                'avg_sentence_length': (12, 20),
                'vocabulary_diversity': 0.5,
                'paragraph_count': (3, 6)
            }
        }

    def analyze_text(self, text: str, text_type: str = 'essay') -> Dict:
        """
        Comprehensive text analysis.

        Args:
            text: The text to analyze
            text_type: Type of text (essay, cover_letter, resume, letter)

        Returns:
            Dictionary containing all analysis metrics
        """
        # Basic counts
        word_count = self._count_words(text)
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        sentence_count = self._count_sentences(text)
        paragraph_count = self._count_paragraphs(text)

        # Advanced metrics
        unique_words = self._count_unique_words(text)
        vocabulary_diversity = unique_words / word_count if word_count > 0 else 0

        avg_word_length = char_count_no_spaces / word_count if word_count > 0 else 0
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0

        # Readability scores
        flesch_reading_ease = self._calculate_flesch_reading_ease(text)
        flesch_kincaid_grade = self._calculate_flesch_kincaid_grade(text)

        # Word frequency
        most_common_words = self._get_most_common_words(text, top_n=10)

        # Comparison to standards
        quality_score = self._compare_to_standards(
            word_count, sentence_count, paragraph_count,
            avg_sentence_length, vocabulary_diversity, text_type
        )

        # Reading time estimate (average reading speed: 200-250 words/minute)
        reading_time_minutes = word_count / 225

        return {
            'word_count': word_count,
            'character_count': char_count,
            'character_count_no_spaces': char_count_no_spaces,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count,
            'unique_words': unique_words,
            'vocabulary_diversity': round(vocabulary_diversity, 3),
            'avg_word_length': round(avg_word_length, 2),
            'avg_sentence_length': round(avg_sentence_length, 2),
            'flesch_reading_ease': round(flesch_reading_ease, 2),
            'flesch_kincaid_grade': round(flesch_kincaid_grade, 2),
            'reading_level': self._get_reading_level(flesch_kincaid_grade),
            'reading_time_minutes': round(reading_time_minutes, 1),
            'most_common_words': most_common_words,
            'quality_score': quality_score,
            'text_type': text_type
        }

    def _count_words(self, text: str) -> int:
        """Count words in text."""
        # Remove extra whitespace and split
        words = text.split()
        # Filter out empty strings and pure punctuation
        words = [w for w in words if w and any(c.isalnum() for c in w)]
        return len(words)

    def _count_sentences(self, text: str) -> int:
        """Count sentences in text."""
        # Split on sentence-ending punctuation
        sentences = re.split(r'[.!?]+', text)
        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

    def _count_paragraphs(self, text: str) -> int:
        """Count paragraphs in text."""
        # Split on double newlines or more
        paragraphs = re.split(r'\n\s*\n', text)
        # Filter out empty strings
        paragraphs = [p.strip() for p in paragraphs if p.strip()]
        return len(paragraphs)

    def _count_unique_words(self, text: str) -> int:
        """Count unique words (case-insensitive)."""
        words = text.lower().split()
        # Remove punctuation
        words = [re.sub(r'[^\w\s]', '', w) for w in words if w]
        # Count unique
        return len(set(words))

    def _count_syllables(self, word: str) -> int:
        """
        Estimate syllable count in a word.
        This is a simplified algorithm.
        """
        word = word.lower()
        vowels = 'aeiouy'
        syllable_count = 0
        previous_was_vowel = False

        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel

        # Adjust for silent 'e'
        if word.endswith('e'):
            syllable_count -= 1

        # Every word has at least one syllable
        if syllable_count == 0:
            syllable_count = 1

        return syllable_count

    def _calculate_flesch_reading_ease(self, text: str) -> float:
        """
        Calculate Flesch Reading Ease score.
        Score: 0-100 (higher is easier to read)
        90-100: Very easy (5th grade)
        60-70: Standard (8th-9th grade)
        0-30: Very difficult (college graduate)
        """
        words = self._count_words(text)
        sentences = self._count_sentences(text)

        if words == 0 or sentences == 0:
            return 0

        # Count syllables in all words
        word_list = text.split()
        total_syllables = sum(self._count_syllables(word) for word in word_list)

        # Flesch Reading Ease formula
        score = 206.835 - 1.015 * (words / sentences) - 84.6 * (total_syllables / words)

        return max(0, min(100, score))  # Clamp between 0 and 100

    def _calculate_flesch_kincaid_grade(self, text: str) -> float:
        """
        Calculate Flesch-Kincaid Grade Level.
        Returns the US school grade level required to understand the text.
        """
        words = self._count_words(text)
        sentences = self._count_sentences(text)

        if words == 0 or sentences == 0:
            return 0

        # Count syllables in all words
        word_list = text.split()
        total_syllables = sum(self._count_syllables(word) for word in word_list)

        # Flesch-Kincaid Grade Level formula
        grade = 0.39 * (words / sentences) + 11.8 * (total_syllables / words) - 15.59

        return max(0, grade)

    def _get_reading_level(self, grade: float) -> str:
        """Convert grade level to reading level category."""
        for level, (min_grade, max_grade) in self.reading_level_standards.items():
            if min_grade <= grade <= max_grade:
                return level.replace('_', ' ').title()
        return 'Unknown'

    def _get_most_common_words(self, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Get the most common words in the text.
        Excludes common stop words.
        """
        # Common stop words to exclude
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'is', 'was', 'are', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these',
            'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
            'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both',
            'few', 'more', 'most', 'other', 'some', 'such', 'than', 'too', 'very'
        }

        # Extract words
        words = text.lower().split()
        # Remove punctuation
        words = [re.sub(r'[^\w]', '', w) for w in words]
        # Filter out stop words and short words
        words = [w for w in words if w and len(w) > 3 and w not in stop_words]

        # Count and return most common
        word_counts = Counter(words)
        return word_counts.most_common(top_n)

    def _compare_to_standards(self, word_count: int, sentence_count: int,
                            paragraph_count: int, avg_sentence_length: float,
                            vocabulary_diversity: float, text_type: str) -> Dict:
        """
        Compare text metrics to quality standards.

        Returns quality score and specific feedback.
        """
        if text_type not in self.quality_standards:
            text_type = 'essay'

        standards = self.quality_standards[text_type]
        score = 100
        feedback = []
        strengths = []

        # Check word count
        if word_count < standards['min_words']:
            score -= 20
            feedback.append(f"Text is too short ({word_count} words). "
                          f"Minimum recommended: {standards['min_words']} words")
        elif word_count > standards['max_words']:
            score -= 10
            feedback.append(f"Text is too long ({word_count} words). "
                          f"Maximum recommended: {standards['max_words']} words")
        elif standards['ideal_words'][0] <= word_count <= standards['ideal_words'][1]:
            strengths.append(f"Excellent word count ({word_count} words)")
        else:
            feedback.append(f"Word count is acceptable but could be optimized. "
                          f"Ideal range: {standards['ideal_words'][0]}-{standards['ideal_words'][1]} words")
            score -= 5

        # Check sentence length
        ideal_min, ideal_max = standards['avg_sentence_length']
        if avg_sentence_length < ideal_min - 5:
            score -= 10
            feedback.append(f"Sentences are too short (avg {avg_sentence_length:.1f} words). "
                          f"This can make writing choppy. Aim for {ideal_min}-{ideal_max} words.")
        elif avg_sentence_length > ideal_max + 10:
            score -= 15
            feedback.append(f"Sentences are too long (avg {avg_sentence_length:.1f} words). "
                          f"Break them up for clarity. Aim for {ideal_min}-{ideal_max} words.")
        elif ideal_min <= avg_sentence_length <= ideal_max:
            strengths.append(f"Good sentence length variety")

        # Check vocabulary diversity
        if vocabulary_diversity < standards['vocabulary_diversity'] - 0.1:
            score -= 15
            feedback.append(f"Low vocabulary diversity ({vocabulary_diversity:.2f}). "
                          f"Try using more varied word choices. "
                          f"Target: {standards['vocabulary_diversity']:.2f}")
        elif vocabulary_diversity >= standards['vocabulary_diversity']:
            strengths.append(f"Excellent vocabulary diversity")

        # Check paragraph count
        ideal_min, ideal_max = standards['paragraph_count']
        if paragraph_count < ideal_min:
            score -= 10
            feedback.append(f"Too few paragraphs ({paragraph_count}). "
                          f"Break text into {ideal_min}-{ideal_max} paragraphs for better structure.")
        elif paragraph_count > ideal_max * 1.5:
            score -= 5
            feedback.append(f"Consider consolidating some paragraphs. "
                          f"Current: {paragraph_count}, Recommended: {ideal_min}-{ideal_max}")
        elif ideal_min <= paragraph_count <= ideal_max:
            strengths.append(f"Well-structured paragraphs")

        # Ensure score doesn't go below 0
        score = max(0, score)

        # Add overall assessment
        if score >= 90:
            assessment = "Excellent - Meets high-quality standards"
        elif score >= 75:
            assessment = "Good - Minor improvements recommended"
        elif score >= 60:
            assessment = "Acceptable - Several areas for improvement"
        else:
            assessment = "Needs work - Significant improvements needed"

        return {
            'score': score,
            'assessment': assessment,
            'feedback': feedback,
            'strengths': strengths
        }

    def compare_texts(self, text1: str, text2: str) -> Dict:
        """
        Compare two texts and show differences in metrics.
        Useful for before/after comparisons.
        """
        analysis1 = self.analyze_text(text1)
        analysis2 = self.analyze_text(text2)

        comparison = {
            'text1_stats': analysis1,
            'text2_stats': analysis2,
            'differences': {}
        }

        # Calculate differences for key metrics
        metrics = ['word_count', 'sentence_count', 'paragraph_count',
                  'vocabulary_diversity', 'avg_sentence_length',
                  'flesch_reading_ease', 'flesch_kincaid_grade']

        for metric in metrics:
            val1 = analysis1[metric]
            val2 = analysis2[metric]
            diff = val2 - val1
            percent_change = (diff / val1 * 100) if val1 != 0 else 0

            comparison['differences'][metric] = {
                'text1': val1,
                'text2': val2,
                'difference': round(diff, 2),
                'percent_change': round(percent_change, 2)
            }

        return comparison


def format_analysis_report(analysis: Dict) -> str:
    """Format text analysis into a readable report."""
    report = []
    report.append("=" * 70)
    report.append("TEXT ANALYSIS REPORT")
    report.append("=" * 70)

    report.append(f"\nTEXT TYPE: {analysis['text_type'].upper()}")
    report.append("\nBASIC STATISTICS:")
    report.append(f"  Word Count:              {analysis['word_count']}")
    report.append(f"  Character Count:         {analysis['character_count']}")
    report.append(f"  Characters (no spaces):  {analysis['character_count_no_spaces']}")
    report.append(f"  Sentence Count:          {analysis['sentence_count']}")
    report.append(f"  Paragraph Count:         {analysis['paragraph_count']}")
    report.append(f"  Unique Words:            {analysis['unique_words']}")

    report.append("\nADVANCED METRICS:")
    report.append(f"  Vocabulary Diversity:    {analysis['vocabulary_diversity']}")
    report.append(f"  Avg Word Length:         {analysis['avg_word_length']} characters")
    report.append(f"  Avg Sentence Length:     {analysis['avg_sentence_length']} words")

    report.append("\nREADABILITY:")
    report.append(f"  Flesch Reading Ease:     {analysis['flesch_reading_ease']}/100")
    report.append(f"  Flesch-Kincaid Grade:    {analysis['flesch_kincaid_grade']}")
    report.append(f"  Reading Level:           {analysis['reading_level']}")
    report.append(f"  Estimated Reading Time:  {analysis['reading_time_minutes']} minutes")

    if analysis['most_common_words']:
        report.append("\nMOST COMMON WORDS:")
        for word, count in analysis['most_common_words']:
            report.append(f"  {word}: {count}")

    report.append("\n" + "-" * 70)
    report.append("QUALITY ASSESSMENT")
    report.append("-" * 70)

    quality = analysis['quality_score']
    report.append(f"\nQuality Score: {quality['score']}/100")
    report.append(f"Assessment: {quality['assessment']}\n")

    if quality['strengths']:
        report.append("STRENGTHS:")
        for strength in quality['strengths']:
            report.append(f"  ✓ {strength}")

    if quality['feedback']:
        report.append("\nAREAS FOR IMPROVEMENT:")
        for i, item in enumerate(quality['feedback'], 1):
            report.append(f"  {i}. {item}")

    report.append("\n" + "=" * 70)

    return "\n".join(report)
