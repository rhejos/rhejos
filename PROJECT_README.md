# Text Analysis & AI Humanizer

A comprehensive Python tool for detecting bias in writing, humanizing AI-generated text, formatting documents in multiple styles, and analyzing text quality.

## Features

### 1. Bias Detection
Evaluates text for various types of bias including:
- **Gender bias**: Detects gendered language, stereotypes, and pronoun imbalances
- **Racial/Ethnic bias**: Identifies coded language and racial stereotypes
- **Age bias**: Catches age-related stereotypes and discriminatory language
- **Political bias**: Detects politically charged or polarizing language
- **Ability bias**: Identifies ableist language and inappropriate disability references
- **Socioeconomic bias**: Catches classist language and stereotypes
- **Language accessibility**: Analyzes readability and complexity

### 2. AI Text Humanization
Transforms AI-generated text into natural, human-like writing:
- Removes AI-typical phrases ("As an AI language model", "It's important to note")
- Eliminates AI symbols and markers (●, ※, 【】, etc.)
- Adds natural contractions
- Reduces overly formal language
- Varies sentence structure
- Adds natural speech patterns
- Analyzes AI probability score

### 3. Multiple Format Support
Formats text according to professional standards:
- **MLA Format**: Academic papers with proper citations and formatting
- **Essay**: Standard essay format with proper structure
- **Letter**: Formal business letter format
- **Cover Letter**: Job application cover letter with all necessary sections
- **Resume/CV**: Professional resume formatting
- **Plain Text**: Basic cleanup and formatting

### 4. Text Analysis & Quality Assessment
Comprehensive text statistics and quality metrics:
- Word count, character count, sentence count, paragraph count
- Vocabulary diversity and unique word analysis
- Average word and sentence length
- Flesch Reading Ease score
- Flesch-Kincaid Grade Level
- Reading time estimates
- Most common words analysis
- Quality comparison to industry standards
- Specific recommendations for improvement

## Installation

```bash
# Clone the repository
git clone https://github.com/rhejos/rhejos.git
cd rhejos

# No external dependencies required!
# All modules use Python standard library only
# Python 3.7+ required
python --version
```

## Usage

### Interactive Mode (Recommended for Beginners)

```bash
python main.py
```

This launches an interactive wizard that guides you through:
1. Text input (paste or type)
2. Feature selection (bias detection, AI analysis, humanization, formatting)
3. Format options (if formatting is selected)
4. Results display
5. Option to save results to file

### Command-Line Mode

```bash
# Basic usage - analyze a file
python main.py -f input.txt

# Detect bias only
python main.py -f input.txt -b

# Humanize AI text
python main.py -f input.txt -h

# Full analysis with all features
python main.py -f input.txt -b -a -h -t essay -o output.txt

# Format as cover letter
python main.py -f input.txt -h -t cover_letter -o formatted_letter.txt
```

### Command-Line Options

```
-f, --file FILE          Input file path
-b, --bias              Detect bias in text
-a, --ai-analysis       Analyze AI likelihood
-h, --humanize          Humanize AI-generated text
-t, --format-type TYPE  Format type (mla, essay, letter, cover_letter, resume, plain)
-o, --output FILE       Output file path
```

### Python API Usage

#### Example 1: Detect Bias

```python
from bias_detector import BiasDetector, format_bias_report

text = "The chairman discussed how mankind needs young blood in the company."

detector = BiasDetector()
results = detector.detect_bias(text)

print(format_bias_report(results))
# Shows detected biases: chairman (gender), mankind (gender), young blood (age)
```

#### Example 2: Humanize AI Text

```python
from ai_humanizer import AIHumanizer

ai_text = """
As an AI language model, I would like to inform you that it is important
to note that climate change is a significant issue. Furthermore, it is
essential to understand that we must take action.
"""

humanizer = AIHumanizer()

# Check AI probability
analysis = humanizer.analyze_ai_likelihood(ai_text)
print(f"AI Probability: {analysis['ai_probability']}%")

# Humanize the text
humanized = humanizer.humanize_text(ai_text)
print(humanized)
# Output: Climate change is a significant issue. We need to take action now.
```

#### Example 3: Format Text

```python
from text_formatter import TextFormatter

text = "Your essay content here..."

formatter = TextFormatter()
formatted = formatter.format_text(
    text,
    'mla',
    author='John Smith',
    instructor='Dr. Jane Doe',
    course='English 101',
    title='My Essay Title'
)

print(formatted)
```

#### Example 4: Analyze Text Quality

```python
from text_analyzer import TextAnalyzer, format_analysis_report

text = "Your text here..."

analyzer = TextAnalyzer()
analysis = analyzer.analyze_text(text, text_type='essay')

print(format_analysis_report(analysis))
# Shows word count, readability scores, quality assessment, etc.
```

#### Example 5: Complete Workflow

```python
from main import TextProcessingApp

app = TextProcessingApp()

text = "Your AI-generated text here..."

options = {
    'detect_bias': True,
    'analyze_ai': True,
    'humanize': True,
    'format_type': 'essay',
    'format_params': {'title': 'My Essay'}
}

results = app.process_text(text, options)
report = app.generate_report(results, options)

print(report)
```

## Running Examples

The project includes comprehensive examples demonstrating all features:

```bash
python example.py
```

This will run through 5 detailed examples:
1. Bias detection demonstration
2. AI humanization demonstration
3. Text formatting in multiple styles
4. Text analysis and statistics
5. Complete workflow combining all features

## Project Structure

```
rhejos/
├── main.py              # Main application entry point
├── bias_detector.py     # Bias detection module
├── ai_humanizer.py      # AI text humanization module
├── text_formatter.py    # Text formatting module
├── text_analyzer.py     # Text analysis and statistics module
├── example.py           # Example usage demonstrations
├── requirements.txt     # Dependencies (none required!)
├── README.md           # Personal profile README
└── PROJECT_README.md   # This file - project documentation
```

## Quality Standards

The tool compares your text against industry standards for different document types:

### Essay Standards
- Word count: 500-1,500 words (ideal)
- Sentence length: 15-20 words average
- Vocabulary diversity: 50%+
- Paragraphs: 3-10

### Cover Letter Standards
- Word count: 250-400 words (ideal)
- Sentence length: 12-18 words average
- Vocabulary diversity: 55%+
- Paragraphs: 3-5

### Resume Standards
- Word count: 300-600 words (ideal)
- Sentence length: 10-15 words average
- Vocabulary diversity: 60%+
- Sections: 4-8

## Understanding Scores

### Bias Score (0-100, lower is better)
- **0-20**: Excellent - Very inclusive language
- **20-40**: Good - Minor bias detected
- **40-60**: Fair - Moderate bias issues
- **60-80**: Poor - Significant bias detected
- **80-100**: Critical - Extensive bias throughout

### AI Probability (0-100)
- **0-20**: Appears very human-like
- **20-40**: Appears mostly human-written
- **40-60**: May be AI-generated or heavily edited
- **60-80**: Likely AI-generated
- **80-100**: Very likely AI-generated

### Quality Score (0-100, higher is better)
- **90-100**: Excellent - Meets high-quality standards
- **75-89**: Good - Minor improvements recommended
- **60-74**: Acceptable - Several areas for improvement
- **0-59**: Needs work - Significant improvements needed

### Readability Scores

**Flesch Reading Ease (0-100)**
- 90-100: Very easy (5th grade)
- 60-70: Standard (8th-9th grade)
- 30-50: Difficult (College level)
- 0-30: Very difficult (Graduate level)

**Flesch-Kincaid Grade Level**
- Direct indication of US school grade level required to understand the text

## Use Cases

### For Students
- Check essays for bias before submission
- Format papers in MLA or other required styles
- Analyze text quality and get improvement suggestions
- Ensure appropriate reading level for target audience

### For Job Seekers
- Humanize AI-generated cover letters
- Format resumes professionally
- Ensure bias-free language in applications
- Optimize word count and structure

### For Content Writers
- Remove AI detection markers from assisted writing
- Ensure inclusive, unbiased content
- Analyze readability for target audience
- Compare text quality to industry standards

### For Editors
- Quick bias detection across multiple documents
- Standardize formatting across submissions
- Quality assessment and improvement recommendations
- Readability analysis for different audiences

## Technical Details

### No External Dependencies
All modules use only Python standard library (re, collections, datetime, etc.). No pip install required!

### Algorithms Used
- **Syllable counting**: Vowel cluster detection algorithm
- **Readability**: Flesch Reading Ease and Flesch-Kincaid Grade Level formulas
- **Bias detection**: Pattern matching against curated bias indicator databases
- **AI detection**: Multi-factor analysis of style patterns, formality, and structure

### Performance
- Processes typical documents (500-2000 words) in under 1 second
- No API calls or external services required
- Runs completely offline

## Limitations

1. **Bias Detection**: Based on pattern matching; may not catch all subtle biases or context-dependent issues
2. **AI Detection**: Heuristic-based; sophisticated AI text may not be detected, and human text with formal style may be flagged
3. **Language**: Currently optimized for English only
4. **Context**: Tools analyze text in isolation; may miss context-dependent meanings

## Contributing

Contributions are welcome! Areas for improvement:
- Additional bias categories
- Support for more formatting styles (APA, Chicago, etc.)
- Multi-language support
- Machine learning-based AI detection
- Additional quality metrics

## License

MIT License - See LICENSE file for details

## Author

**Rhea Joseph**
- Data Engineer with expertise in Python, Data Pipelines, and Data Governance
- LinkedIn: [rheajoseph](https://www.linkedin.com/in/rheajoseph/)
- GitHub: [@rhejos](https://github.com/rhejos)

## Support

For issues, questions, or suggestions:
1. Open an issue on GitHub
2. Check existing examples in `example.py`
3. Review this documentation

## Changelog

### Version 1.0.0 (2025)
- Initial release
- Bias detection for 6 bias categories
- AI text humanization with 15+ transformation rules
- Support for 6 document formats
- Comprehensive text analysis and quality assessment
- Interactive and command-line interfaces
- Complete example demonstrations

---

**Made with ❤️ for better, more inclusive, and more human writing**
