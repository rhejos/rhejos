"""
Bias Detection Module
Evaluates text for various types of bias including gender, racial, political, and other biases.
"""

import re
from typing import Dict, List, Tuple
from collections import defaultdict


class BiasDetector:
    def __init__(self):
        # Gender bias indicators
        self.gender_biased_terms = {
            'male': ['mankind', 'manpower', 'chairman', 'policeman', 'fireman',
                    'businessman', 'spokesman', 'workman', 'salesman', 'mailman',
                    'he/him (generic)', 'guys (generic)'],
            'female': ['emotional', 'bossy', 'feisty', 'high-maintenance', 'shrill',
                      'hysterical', 'hormonal', 'sassy'],
            'stereotypical': ['lady doctor', 'male nurse', 'female engineer',
                            'working mother', 'career woman']
        }

        # Racial/ethnic bias indicators
        self.racial_bias_terms = [
            'exotic', 'articulate (in racial context)', 'urban', 'inner-city',
            'ethnic-sounding name', 'well-spoken (in racial context)', 'minority',
            'diverse (as euphemism)', 'ghetto', 'thug'
        ]

        # Age bias indicators
        self.age_bias_terms = [
            'young blood', 'old-timer', 'overqualified', 'digital native',
            'senior moment', 'past their prime', 'fresh perspective',
            'too experienced', 'not enough experience'
        ]

        # Political bias indicators
        self.political_bias_words = {
            'left-leaning': ['fascist', 'nazi', 'right-wing extremist', 'conservative bias'],
            'right-leaning': ['communist', 'socialist', 'left-wing radical', 'liberal bias'],
            'polarizing': ['fake news', 'brainwashed', 'sheep', 'woke', 'snowflake']
        }

        # Ability bias indicators
        self.ability_bias_terms = [
            'handicapped', 'crippled', 'suffers from', 'victim of', 'confined to wheelchair',
            'special needs', 'differently abled', 'mentally challenged', 'crazy', 'insane',
            'lame', 'dumb', 'blind to', 'deaf to'
        ]

        # Socioeconomic bias
        self.socioeconomic_bias_terms = [
            'poor', 'disadvantaged', 'underprivileged', 'low-class', 'trailer trash',
            'white trash', 'welfare queen', 'born with silver spoon'
        ]

    def detect_bias(self, text: str) -> Dict:
        """
        Comprehensive bias detection in text.
        Returns a dictionary with bias scores and specific issues found.
        """
        text_lower = text.lower()

        results = {
            'overall_bias_score': 0,
            'gender_bias': self._check_gender_bias(text, text_lower),
            'racial_bias': self._check_racial_bias(text_lower),
            'age_bias': self._check_age_bias(text_lower),
            'political_bias': self._check_political_bias(text_lower),
            'ability_bias': self._check_ability_bias(text_lower),
            'socioeconomic_bias': self._check_socioeconomic_bias(text_lower),
            'language_complexity': self._check_language_complexity(text),
            'inclusivity_score': 0,
            'recommendations': []
        }

        # Calculate overall bias score (0-100, lower is better)
        bias_count = sum([
            len(results['gender_bias']['issues']),
            len(results['racial_bias']['issues']),
            len(results['age_bias']['issues']),
            len(results['political_bias']['issues']),
            len(results['ability_bias']['issues']),
            len(results['socioeconomic_bias']['issues'])
        ])

        # Normalize score
        text_length = len(text.split())
        if text_length > 0:
            results['overall_bias_score'] = min(100, (bias_count / text_length) * 1000)

        results['inclusivity_score'] = max(0, 100 - results['overall_bias_score'])

        # Generate recommendations
        results['recommendations'] = self._generate_recommendations(results)

        return results

    def _check_gender_bias(self, text: str, text_lower: str) -> Dict:
        """Check for gender bias in text."""
        issues = []

        for category, terms in self.gender_biased_terms.items():
            for term in terms:
                term_lower = term.split('(')[0].strip().lower()
                if term_lower in text_lower:
                    issues.append({
                        'term': term,
                        'category': category,
                        'severity': 'medium'
                    })

        # Check for pronoun usage patterns
        he_count = len(re.findall(r'\bhe\b|\bhim\b|\bhis\b', text_lower))
        she_count = len(re.findall(r'\bshe\b|\bher\b|\bhers\b', text_lower))

        if he_count > she_count * 2 or she_count > he_count * 2:
            issues.append({
                'term': 'Pronoun imbalance',
                'category': 'pronoun_bias',
                'severity': 'low',
                'details': f'He/Him: {he_count}, She/Her: {she_count}'
            })

        return {
            'score': len(issues),
            'issues': issues
        }

    def _check_racial_bias(self, text_lower: str) -> Dict:
        """Check for racial/ethnic bias."""
        issues = []

        for term in self.racial_bias_terms:
            term_lower = term.split('(')[0].strip().lower()
            if term_lower in text_lower:
                issues.append({
                    'term': term,
                    'severity': 'high'
                })

        return {
            'score': len(issues),
            'issues': issues
        }

    def _check_age_bias(self, text_lower: str) -> Dict:
        """Check for age-related bias."""
        issues = []

        for term in self.age_bias_terms:
            if term.lower() in text_lower:
                issues.append({
                    'term': term,
                    'severity': 'medium'
                })

        return {
            'score': len(issues),
            'issues': issues
        }

    def _check_political_bias(self, text_lower: str) -> Dict:
        """Check for political bias."""
        issues = []

        for leaning, terms in self.political_bias_words.items():
            for term in terms:
                if term.lower() in text_lower:
                    issues.append({
                        'term': term,
                        'leaning': leaning,
                        'severity': 'high'
                    })

        return {
            'score': len(issues),
            'issues': issues
        }

    def _check_ability_bias(self, text_lower: str) -> Dict:
        """Check for ability/disability bias."""
        issues = []

        for term in self.ability_bias_terms:
            if term.lower() in text_lower:
                issues.append({
                    'term': term,
                    'severity': 'medium'
                })

        return {
            'score': len(issues),
            'issues': issues
        }

    def _check_socioeconomic_bias(self, text_lower: str) -> Dict:
        """Check for socioeconomic bias."""
        issues = []

        for term in self.socioeconomic_bias_terms:
            if term.lower() in text_lower:
                issues.append({
                    'term': term,
                    'severity': 'high'
                })

        return {
            'score': len(issues),
            'issues': issues
        }

    def _check_language_complexity(self, text: str) -> Dict:
        """
        Check if language is accessible or overly complex.
        Complex language can be a form of bias against those with different education levels.
        """
        words = text.split()
        long_words = [w for w in words if len(w) > 10]
        avg_word_length = sum(len(w) for w in words) / len(words) if words else 0

        sentences = re.split(r'[.!?]+', text)
        avg_sentence_length = len(words) / len(sentences) if sentences else 0

        return {
            'avg_word_length': round(avg_word_length, 2),
            'avg_sentence_length': round(avg_sentence_length, 2),
            'long_words_count': len(long_words),
            'readability': 'complex' if avg_word_length > 6 or avg_sentence_length > 25 else 'accessible'
        }

    def _generate_recommendations(self, results: Dict) -> List[str]:
        """Generate specific recommendations based on detected biases."""
        recommendations = []

        if results['gender_bias']['score'] > 0:
            recommendations.append("Use gender-neutral language (e.g., 'chairperson' instead of 'chairman', 'humanity' instead of 'mankind')")
            recommendations.append("Consider using 'they/them' as singular pronouns or alternate between gender pronouns")

        if results['racial_bias']['score'] > 0:
            recommendations.append("Replace coded language with specific, neutral descriptions")
            recommendations.append("Avoid terms that may carry racial stereotypes or implications")

        if results['age_bias']['score'] > 0:
            recommendations.append("Focus on skills and qualifications rather than age-related characteristics")
            recommendations.append("Avoid age-related stereotypes or assumptions")

        if results['political_bias']['score'] > 0:
            recommendations.append("Use neutral, fact-based language instead of politically charged terms")
            recommendations.append("Present multiple perspectives when discussing contentious topics")

        if results['ability_bias']['score'] > 0:
            recommendations.append("Use person-first language (e.g., 'person with a disability' rather than 'disabled person')")
            recommendations.append("Avoid metaphorical use of disability terms")

        if results['socioeconomic_bias']['score'] > 0:
            recommendations.append("Use respectful, non-judgmental language when discussing economic status")
            recommendations.append("Avoid stereotypes about socioeconomic groups")

        if results['language_complexity']['readability'] == 'complex':
            recommendations.append("Simplify language for better accessibility and inclusivity")
            recommendations.append("Break long sentences into shorter, clearer statements")

        if not recommendations:
            recommendations.append("Great job! No significant bias detected. Continue using inclusive language.")

        return recommendations


def format_bias_report(results: Dict) -> str:
    """Format the bias detection results into a readable report."""
    report = []
    report.append("=" * 60)
    report.append("BIAS DETECTION REPORT")
    report.append("=" * 60)
    report.append(f"\nOverall Bias Score: {results['overall_bias_score']:.2f}/100")
    report.append(f"Inclusivity Score: {results['inclusivity_score']:.2f}/100")
    report.append("\n" + "-" * 60)

    # Gender Bias
    report.append("\nGENDER BIAS:")
    if results['gender_bias']['issues']:
        for issue in results['gender_bias']['issues']:
            report.append(f"  - {issue['term']} [{issue['severity']}]")
    else:
        report.append("  ✓ No gender bias detected")

    # Racial Bias
    report.append("\nRACIAL/ETHNIC BIAS:")
    if results['racial_bias']['issues']:
        for issue in results['racial_bias']['issues']:
            report.append(f"  - {issue['term']} [{issue['severity']}]")
    else:
        report.append("  ✓ No racial bias detected")

    # Age Bias
    report.append("\nAGE BIAS:")
    if results['age_bias']['issues']:
        for issue in results['age_bias']['issues']:
            report.append(f"  - {issue['term']} [{issue['severity']}]")
    else:
        report.append("  ✓ No age bias detected")

    # Political Bias
    report.append("\nPOLITICAL BIAS:")
    if results['political_bias']['issues']:
        for issue in results['political_bias']['issues']:
            report.append(f"  - {issue['term']} [{issue['severity']}]")
    else:
        report.append("  ✓ No political bias detected")

    # Ability Bias
    report.append("\nABILITY/DISABILITY BIAS:")
    if results['ability_bias']['issues']:
        for issue in results['ability_bias']['issues']:
            report.append(f"  - {issue['term']} [{issue['severity']}]")
    else:
        report.append("  ✓ No ability bias detected")

    # Socioeconomic Bias
    report.append("\nSOCIOECONOMIC BIAS:")
    if results['socioeconomic_bias']['issues']:
        for issue in results['socioeconomic_bias']['issues']:
            report.append(f"  - {issue['term']} [{issue['severity']}]")
    else:
        report.append("  ✓ No socioeconomic bias detected")

    # Language Complexity
    report.append("\nLANGUAGE ACCESSIBILITY:")
    complexity = results['language_complexity']
    report.append(f"  - Average word length: {complexity['avg_word_length']}")
    report.append(f"  - Average sentence length: {complexity['avg_sentence_length']} words")
    report.append(f"  - Readability: {complexity['readability']}")

    # Recommendations
    report.append("\n" + "-" * 60)
    report.append("\nRECOMMENDATIONS:")
    for i, rec in enumerate(results['recommendations'], 1):
        report.append(f"{i}. {rec}")

    report.append("\n" + "=" * 60)

    return "\n".join(report)
