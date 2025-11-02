"""
AI Text Humanizer Module
Transforms AI-sounding text into more natural, human-like writing.
Removes typical AI markers and improves authenticity.
"""

import re
import random
from typing import List, Dict


class AIHumanizer:
    def __init__(self):
        # Common AI phrases to replace
        self.ai_phrases = {
            'As an AI language model': '',
            'I apologize, but': '',
            'It\'s important to note that': '',
            'It is worth noting that': '',
            'In conclusion': 'To wrap up',
            'Furthermore': ['Also', 'Plus', 'Additionally', 'On top of that'],
            'Moreover': ['Also', 'Besides', 'What\'s more'],
            'Nevertheless': ['Still', 'Even so', 'That said'],
            'Therefore': ['So', 'Thus', 'That\'s why'],
            'However': ['But', 'Yet', 'Though', 'Still'],
            'Additionally': ['Also', 'Plus', 'And'],
            'Subsequently': ['Then', 'After that', 'Later'],
            'Consequently': ['As a result', 'So', 'Because of this'],
            'In order to': 'To',
            'Due to the fact that': 'Because',
            'In the event that': 'If',
            'For the purpose of': 'For',
            'With regard to': 'About',
            'In terms of': 'For',
            'It should be noted that': '',
            'One must consider': 'Consider',
            'It is essential to': 'You should',
            'It is crucial to': 'You need to'
        }

        # AI writing patterns to modify
        self.formal_contractions = {
            'do not': 'don\'t',
            'does not': 'doesn\'t',
            'is not': 'isn\'t',
            'are not': 'aren\'t',
            'was not': 'wasn\'t',
            'were not': 'weren\'t',
            'have not': 'haven\'t',
            'has not': 'hasn\'t',
            'will not': 'won\'t',
            'would not': 'wouldn\'t',
            'should not': 'shouldn\'t',
            'could not': 'couldn\'t',
            'cannot': 'can\'t',
            'it is': 'it\'s',
            'that is': 'that\'s',
            'there is': 'there\'s',
            'what is': 'what\'s',
            'who is': 'who\'s',
            'they are': 'they\'re',
            'we are': 'we\'re',
            'you are': 'you\'re'
        }

        # Overly formal words to replace
        self.formal_words = {
            'utilize': 'use',
            'endeavor': 'try',
            'facilitate': 'help',
            'implement': 'do',
            'ascertain': 'find out',
            'commence': 'start',
            'terminate': 'end',
            'obtain': 'get',
            'purchase': 'buy',
            'provide': 'give',
            'assist': 'help',
            'require': 'need',
            'sufficient': 'enough',
            'numerous': 'many',
            'prior to': 'before',
            'subsequent to': 'after',
            'concerning': 'about',
            'regarding': 'about',
            'aforementioned': 'mentioned',
            'heretofore': 'until now',
            'in lieu of': 'instead of'
        }

        # Symbols commonly used by AI
        self.ai_symbols = [
            '※', '★', '☆', '●', '○', '■', '□', '▪', '▫',
            '✓', '✔', '✕', '✖', '✗', '✘',
            '➤', '➔', '➜', '➡', '⇒', '⟹',
            '【', '】', '『', '』', '「', '」'
        ]

    def humanize_text(self, text: str, preserve_formatting: bool = True) -> str:
        """
        Main method to humanize AI-generated text.

        Args:
            text: The text to humanize
            preserve_formatting: Whether to preserve original formatting

        Returns:
            Humanized text
        """
        humanized = text

        # Remove AI-specific symbols
        humanized = self._remove_ai_symbols(humanized)

        # Replace AI phrases
        humanized = self._replace_ai_phrases(humanized)

        # Make text less formal
        humanized = self._reduce_formality(humanized)

        # Add contractions
        humanized = self._add_contractions(humanized)

        # Vary sentence structure
        humanized = self._vary_sentence_structure(humanized)

        # Remove excessive politeness
        humanized = self._reduce_politeness(humanized)

        # Add minor imperfections (optional - makes it more human)
        humanized = self._add_natural_elements(humanized)

        # Clean up extra spaces and formatting
        humanized = self._clean_formatting(humanized)

        return humanized

    def _remove_ai_symbols(self, text: str) -> str:
        """Remove symbols typically used by AI."""
        for symbol in self.ai_symbols:
            text = text.replace(symbol, '')

        # Remove excessive bullet points that AI loves
        # Replace multiple bullet formats with simple dashes
        text = re.sub(r'[●○■□▪▫]', '-', text)

        return text

    def _replace_ai_phrases(self, text: str) -> str:
        """Replace common AI phrases with more natural alternatives."""
        for phrase, replacement in self.ai_phrases.items():
            if isinstance(replacement, list):
                # Choose a random replacement for variety
                if phrase in text:
                    text = text.replace(phrase, random.choice(replacement))
            else:
                text = text.replace(phrase, replacement)

        return text

    def _reduce_formality(self, text: str) -> str:
        """Replace overly formal words with casual alternatives."""
        words = text.split()
        new_words = []

        for word in words:
            # Check if word (without punctuation) is in formal words
            clean_word = word.lower().strip('.,!?;:')
            if clean_word in self.formal_words:
                # Preserve original punctuation
                punct = ''.join(c for c in word if c in '.,!?;:')
                new_word = self.formal_words[clean_word]
                # Preserve original capitalization
                if word[0].isupper():
                    new_word = new_word.capitalize()
                new_words.append(new_word + punct)
            else:
                new_words.append(word)

        return ' '.join(new_words)

    def _add_contractions(self, text: str) -> str:
        """Add contractions to make text sound more natural."""
        for formal, contracted in self.formal_contractions.items():
            # Case-insensitive replacement
            pattern = re.compile(r'\b' + formal + r'\b', re.IGNORECASE)
            text = pattern.sub(contracted, text)

        return text

    def _vary_sentence_structure(self, text: str) -> str:
        """
        Vary sentence structure to sound more natural.
        AI tends to use very consistent sentence structures.
        """
        # Break up very long sentences (AI loves compound sentences)
        sentences = re.split(r'([.!?]+)', text)

        new_sentences = []
        for i in range(0, len(sentences) - 1, 2):
            sentence = sentences[i]
            punct = sentences[i + 1] if i + 1 < len(sentences) else '.'

            # If sentence is very long and has multiple clauses, consider breaking it
            if len(sentence.split()) > 30 and ',' in sentence:
                # Find a good breaking point
                parts = sentence.split(',')
                if len(parts) >= 2:
                    # Break after first major clause
                    new_sentences.append(parts[0].strip() + '.')
                    remaining = ','.join(parts[1:]).strip()
                    if remaining:
                        # Capitalize first letter
                        remaining = remaining[0].upper() + remaining[1:]
                        new_sentences.append(remaining + punct)
                    continue

            new_sentences.append(sentence + punct)

        return ' '.join(new_sentences)

    def _reduce_politeness(self, text: str) -> str:
        """Reduce excessive politeness that AI often exhibits."""
        overly_polite = [
            'I would like to',
            'I would be happy to',
            'I would be glad to',
            'If you would like',
            'Please feel free to',
            'I hope this helps',
            'I hope this information is helpful'
        ]

        replacements = [
            'I want to',
            'I can',
            'I can',
            'If you want',
            'Feel free to',
            '',
            ''
        ]

        for i, phrase in enumerate(overly_polite):
            text = text.replace(phrase, replacements[i])

        return text

    def _add_natural_elements(self, text: str) -> str:
        """
        Add elements that make text feel more human.
        This includes minor variations and natural speech patterns.
        """
        # Add occasional interjections (sparingly)
        interjections = ['Well, ', 'So, ', 'Now, ', 'Look, ', 'Actually, ']

        sentences = text.split('. ')
        if len(sentences) > 3:
            # Add an interjection to one random sentence (not the first)
            idx = random.randint(1, min(len(sentences) - 1, 3))
            if not sentences[idx].startswith(tuple(interjections)):
                sentences[idx] = random.choice(interjections) + sentences[idx]

        text = '. '.join(sentences)

        # Replace some "very" with stronger adjectives
        very_replacements = {
            'very good': ['great', 'excellent', 'fantastic'],
            'very bad': ['terrible', 'awful', 'horrible'],
            'very big': ['huge', 'massive', 'enormous'],
            'very small': ['tiny', 'minuscule'],
            'very important': ['crucial', 'vital', 'essential'],
            'very interesting': ['fascinating', 'intriguing']
        }

        for phrase, replacements in very_replacements.items():
            if phrase in text.lower():
                text = re.sub(phrase, random.choice(replacements), text, flags=re.IGNORECASE)

        return text

    def _clean_formatting(self, text: str) -> str:
        """Clean up formatting issues."""
        # Remove multiple spaces
        text = re.sub(r' +', ' ', text)

        # Remove spaces before punctuation
        text = re.sub(r' ([.,!?;:])', r'\1', text)

        # Ensure space after punctuation
        text = re.sub(r'([.,!?;:])([A-Za-z])', r'\1 \2', text)

        # Remove multiple blank lines
        text = re.sub(r'\n\n+', '\n\n', text)

        # Fix sentence spacing
        text = re.sub(r'\. +([A-Z])', r'. \1', text)

        return text.strip()

    def analyze_ai_likelihood(self, text: str) -> Dict:
        """
        Analyze how AI-like the text appears.
        Returns metrics and AI probability.
        """
        score = 0
        indicators = []

        # Check for AI phrases
        ai_phrase_count = 0
        for phrase in self.ai_phrases.keys():
            if phrase.lower() in text.lower():
                ai_phrase_count += 1
                indicators.append(f"Contains AI phrase: '{phrase}'")

        score += ai_phrase_count * 15

        # Check for AI symbols
        ai_symbol_count = sum(1 for symbol in self.ai_symbols if symbol in text)
        if ai_symbol_count > 0:
            score += ai_symbol_count * 10
            indicators.append(f"Contains {ai_symbol_count} AI-typical symbols")

        # Check formality level
        formal_word_count = sum(1 for word in self.formal_words.keys()
                                if word in text.lower())
        if formal_word_count > 3:
            score += formal_word_count * 5
            indicators.append(f"High formality: {formal_word_count} formal words")

        # Check for lack of contractions
        word_count = len(text.split())
        contraction_count = sum(1 for word in text.split() if "'" in word)
        if word_count > 50 and contraction_count == 0:
            score += 20
            indicators.append("No contractions used (overly formal)")

        # Check sentence structure uniformity
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if sentences:
            avg_length = sum(len(s.split()) for s in sentences) / len(sentences)
            if avg_length > 25:
                score += 15
                indicators.append(f"Very long average sentence length: {avg_length:.1f} words")

        # Check for repetitive structure
        sentence_starts = [s.split()[0] for s in sentences if s.split()]
        if len(sentence_starts) != len(set(sentence_starts)) and len(sentence_starts) > 3:
            score += 10
            indicators.append("Repetitive sentence structures")

        # Normalize score to 0-100
        ai_probability = min(100, score)

        return {
            'ai_probability': ai_probability,
            'assessment': self._get_ai_assessment(ai_probability),
            'indicators': indicators,
            'recommendations': self._get_humanization_recommendations(ai_probability)
        }

    def _get_ai_assessment(self, probability: float) -> str:
        """Get text assessment based on AI probability."""
        if probability < 20:
            return "Appears very human-like"
        elif probability < 40:
            return "Appears mostly human-written"
        elif probability < 60:
            return "May be AI-generated or heavily edited"
        elif probability < 80:
            return "Likely AI-generated"
        else:
            return "Very likely AI-generated"

    def _get_humanization_recommendations(self, probability: float) -> List[str]:
        """Get recommendations for humanizing the text."""
        if probability < 20:
            return ["Text already appears natural!"]

        recommendations = []
        if probability >= 40:
            recommendations.append("Add contractions to sound more conversational")
            recommendations.append("Replace formal words with simpler alternatives")
            recommendations.append("Vary sentence structure and length")

        if probability >= 60:
            recommendations.append("Remove AI-typical phrases and symbols")
            recommendations.append("Break up long, complex sentences")
            recommendations.append("Add more personal voice and natural expressions")

        return recommendations


def format_ai_analysis_report(analysis: Dict) -> str:
    """Format AI likelihood analysis into a readable report."""
    report = []
    report.append("=" * 60)
    report.append("AI TEXT ANALYSIS REPORT")
    report.append("=" * 60)
    report.append(f"\nAI Probability Score: {analysis['ai_probability']:.1f}/100")
    report.append(f"Assessment: {analysis['assessment']}")

    if analysis['indicators']:
        report.append("\nAI INDICATORS DETECTED:")
        for indicator in analysis['indicators']:
            report.append(f"  - {indicator}")
    else:
        report.append("\n✓ No significant AI indicators detected")

    report.append("\nRECOMMENDATIONS:")
    for i, rec in enumerate(analysis['recommendations'], 1):
        report.append(f"{i}. {rec}")

    report.append("\n" + "=" * 60)

    return "\n".join(report)
