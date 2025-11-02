"""
Text Formatter Module
Formats text according to different standards: MLA, Essay, Letter, Cover Letter, Resume.
"""

import re
from datetime import datetime
from typing import Dict, Optional, List


class TextFormatter:
    def __init__(self):
        self.formats = {
            'mla': self._format_mla,
            'essay': self._format_essay,
            'letter': self._format_letter,
            'cover_letter': self._format_cover_letter,
            'resume': self._format_resume,
            'plain': self._format_plain
        }

    def format_text(self, text: str, format_type: str, **kwargs) -> str:
        """
        Format text according to specified format.

        Args:
            text: The text content to format
            format_type: Type of formatting (mla, essay, letter, cover_letter, resume, plain)
            **kwargs: Additional parameters for specific formats

        Returns:
            Formatted text
        """
        format_type = format_type.lower()

        if format_type not in self.formats:
            raise ValueError(f"Unknown format type: {format_type}. "
                           f"Available formats: {', '.join(self.formats.keys())}")

        formatter = self.formats[format_type]
        return formatter(text, **kwargs)

    def _format_mla(self, text: str, **kwargs) -> str:
        """
        Format text in MLA (Modern Language Association) style.

        Expected kwargs:
            - author: Author name
            - instructor: Instructor/Professor name
            - course: Course name/number
            - title: Paper title
            - date: Date (defaults to today)
        """
        author = kwargs.get('author', '[Your Name]')
        instructor = kwargs.get('instructor', '[Instructor Name]')
        course = kwargs.get('course', '[Course Name]')
        title = kwargs.get('title', '[Paper Title]')
        date = kwargs.get('date', datetime.now().strftime('%d %B %Y'))

        # MLA header (left-aligned)
        header = f"{author}\n"
        header += f"{instructor}\n"
        header += f"{course}\n"
        header += f"{date}\n\n"

        # Title (centered)
        centered_title = title.center(80) + "\n\n"

        # Format paragraphs with proper indentation
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []

        for para in paragraphs:
            if para.strip():
                # Remove extra whitespace
                para = ' '.join(para.split())
                # Indent first line
                formatted_para = '     ' + para
                formatted_paragraphs.append(formatted_para)

        body = '\n\n'.join(formatted_paragraphs)

        # Combine all parts
        formatted_text = header + centered_title + body

        # Add page numbers (placeholder)
        formatted_text += f"\n\n\n{author} "

        return formatted_text

    def _format_essay(self, text: str, **kwargs) -> str:
        """
        Format text as a standard essay.

        Expected kwargs:
            - title: Essay title
            - author: Author name (optional)
            - include_intro: Whether to emphasize intro paragraph (default: True)
        """
        title = kwargs.get('title', '[Essay Title]')
        author = kwargs.get('author', '')
        include_intro = kwargs.get('include_intro', True)

        # Title (centered and bold-marked)
        formatted = title.upper().center(80) + "\n"

        if author:
            formatted += f"\nBy {author}\n"

        formatted += "\n\n"

        # Format paragraphs
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []

        for i, para in enumerate(paragraphs):
            if para.strip():
                # Clean up paragraph
                para = ' '.join(para.split())

                # Add indentation
                formatted_para = '    ' + para

                # Add extra spacing for intro paragraph if requested
                if i == 0 and include_intro:
                    formatted_para = formatted_para + "\n"

                formatted_paragraphs.append(formatted_para)

        body = '\n\n'.join(formatted_paragraphs)
        formatted += body

        return formatted

    def _format_letter(self, text: str, **kwargs) -> str:
        """
        Format text as a formal letter.

        Expected kwargs:
            - sender_name: Name of sender
            - sender_address: Address of sender
            - recipient_name: Name of recipient
            - recipient_address: Address of recipient
            - date: Date (defaults to today)
            - subject: Subject line (optional)
            - closing: Closing phrase (defaults to 'Sincerely')
        """
        sender_name = kwargs.get('sender_name', '[Your Name]')
        sender_address = kwargs.get('sender_address', '[Your Address]')
        recipient_name = kwargs.get('recipient_name', '[Recipient Name]')
        recipient_address = kwargs.get('recipient_address', '[Recipient Address]')
        date = kwargs.get('date', datetime.now().strftime('%B %d, %Y'))
        subject = kwargs.get('subject', '')
        closing = kwargs.get('closing', 'Sincerely')

        # Sender's address (right-aligned or left-aligned based on preference)
        formatted = f"{sender_name}\n{sender_address}\n\n"

        # Date
        formatted += f"{date}\n\n"

        # Recipient's address
        formatted += f"{recipient_name}\n{recipient_address}\n\n"

        # Subject (optional)
        if subject:
            formatted += f"Subject: {subject}\n\n"

        # Greeting
        formatted += f"Dear {recipient_name},\n\n"

        # Body
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []

        for para in paragraphs:
            if para.strip():
                # Clean up paragraph
                para = ' '.join(para.split())
                formatted_paragraphs.append(para)

        body = '\n\n'.join(formatted_paragraphs)
        formatted += body

        # Closing
        formatted += f"\n\n{closing},\n\n\n{sender_name}"

        return formatted

    def _format_cover_letter(self, text: str, **kwargs) -> str:
        """
        Format text as a cover letter for job applications.

        Expected kwargs:
            - your_name: Your name
            - your_address: Your address
            - your_phone: Your phone number
            - your_email: Your email
            - company_name: Company name
            - hiring_manager: Hiring manager name
            - company_address: Company address
            - position: Position applying for
            - date: Date (defaults to today)
        """
        your_name = kwargs.get('your_name', '[Your Name]')
        your_address = kwargs.get('your_address', '[Your Address]')
        your_phone = kwargs.get('your_phone', '[Your Phone]')
        your_email = kwargs.get('your_email', '[Your Email]')
        company_name = kwargs.get('company_name', '[Company Name]')
        hiring_manager = kwargs.get('hiring_manager', 'Hiring Manager')
        company_address = kwargs.get('company_address', '[Company Address]')
        position = kwargs.get('position', '[Position Title]')
        date = kwargs.get('date', datetime.now().strftime('%B %d, %Y'))

        # Your contact information
        formatted = f"{your_name}\n"
        formatted += f"{your_address}\n"
        formatted += f"{your_phone}\n"
        formatted += f"{your_email}\n\n"

        # Date
        formatted += f"{date}\n\n"

        # Company information
        formatted += f"{hiring_manager}\n"
        formatted += f"{company_name}\n"
        formatted += f"{company_address}\n\n"

        # Subject/Position
        formatted += f"Re: Application for {position}\n\n"

        # Salutation
        if hiring_manager != 'Hiring Manager':
            formatted += f"Dear {hiring_manager},\n\n"
        else:
            formatted += "Dear Hiring Manager,\n\n"

        # Body paragraphs
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []

        for para in paragraphs:
            if para.strip():
                # Clean up paragraph
                para = ' '.join(para.split())
                formatted_paragraphs.append(para)

        # Ensure we have intro, body, and closing paragraphs
        body = '\n\n'.join(formatted_paragraphs)
        formatted += body

        # Professional closing
        formatted += "\n\nThank you for your time and consideration. "
        formatted += "I look forward to the opportunity to discuss how I can contribute to your team.\n\n"
        formatted += "Sincerely,\n\n"
        formatted += your_name

        return formatted

    def _format_resume(self, text: str, **kwargs) -> str:
        """
        Format text as a resume/CV.

        Expected kwargs:
            - name: Full name
            - contact: Contact information (phone, email, address)
            - sections: Dict of section names and their content
        """
        name = kwargs.get('name', '[Your Name]')
        contact = kwargs.get('contact', '[Phone] | [Email] | [Address]')

        # Header with name (centered and prominent)
        formatted = "\n"
        formatted += name.upper().center(80) + "\n"
        formatted += contact.center(80) + "\n"
        formatted += "=" * 80 + "\n\n"

        # Standard resume sections
        sections = kwargs.get('sections', {})

        if not sections:
            # If no sections provided, try to parse from text
            formatted += self._parse_resume_sections(text)
        else:
            # Format each section
            for section_name, section_content in sections.items():
                formatted += f"{section_name.upper()}\n"
                formatted += "-" * 40 + "\n"
                formatted += section_content.strip() + "\n\n"

        return formatted

    def _parse_resume_sections(self, text: str) -> str:
        """
        Parse and format resume sections from plain text.
        Looks for common section headers.
        """
        common_sections = [
            'professional summary', 'summary', 'objective',
            'experience', 'work experience', 'professional experience',
            'education', 'skills', 'technical skills',
            'certifications', 'projects', 'achievements',
            'awards', 'publications', 'languages'
        ]

        formatted = ""
        lines = text.split('\n')
        current_section = None
        section_content = []

        for line in lines:
            line_lower = line.lower().strip()

            # Check if line is a section header
            is_section = False
            for section in common_sections:
                if section in line_lower and len(line_lower) < 50:
                    # Save previous section
                    if current_section:
                        formatted += f"{current_section.upper()}\n"
                        formatted += "-" * 40 + "\n"
                        formatted += '\n'.join(section_content) + "\n\n"

                    # Start new section
                    current_section = line.strip()
                    section_content = []
                    is_section = True
                    break

            if not is_section and line.strip():
                section_content.append(line)

        # Add last section
        if current_section:
            formatted += f"{current_section.upper()}\n"
            formatted += "-" * 40 + "\n"
            formatted += '\n'.join(section_content) + "\n\n"

        # If no sections found, just return formatted text
        if not formatted:
            formatted = text

        return formatted

    def _format_plain(self, text: str, **kwargs) -> str:
        """
        Format text as plain text with basic cleanup.
        Just ensures consistent spacing and line breaks.
        """
        # Remove excessive whitespace
        text = re.sub(r' +', ' ', text)

        # Ensure consistent paragraph spacing
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []

        for para in paragraphs:
            if para.strip():
                # Clean up paragraph
                para = ' '.join(para.split())
                formatted_paragraphs.append(para)

        return '\n\n'.join(formatted_paragraphs)

    def get_format_requirements(self, format_type: str) -> Dict:
        """
        Get the required and optional parameters for a format type.
        """
        requirements = {
            'mla': {
                'required': [],
                'optional': ['author', 'instructor', 'course', 'title', 'date'],
                'description': 'MLA format for academic papers'
            },
            'essay': {
                'required': [],
                'optional': ['title', 'author', 'include_intro'],
                'description': 'Standard essay format'
            },
            'letter': {
                'required': [],
                'optional': ['sender_name', 'sender_address', 'recipient_name',
                           'recipient_address', 'date', 'subject', 'closing'],
                'description': 'Formal letter format'
            },
            'cover_letter': {
                'required': [],
                'optional': ['your_name', 'your_address', 'your_phone', 'your_email',
                           'company_name', 'hiring_manager', 'company_address',
                           'position', 'date'],
                'description': 'Job application cover letter format'
            },
            'resume': {
                'required': [],
                'optional': ['name', 'contact', 'sections'],
                'description': 'Professional resume/CV format'
            },
            'plain': {
                'required': [],
                'optional': [],
                'description': 'Plain text with basic formatting'
            }
        }

        return requirements.get(format_type.lower(), {})

    def list_available_formats(self) -> List[str]:
        """Return list of available format types."""
        return list(self.formats.keys())


def format_text_with_style(text: str, format_type: str, **kwargs) -> str:
    """
    Convenience function to format text.

    Args:
        text: Text to format
        format_type: Format type (mla, essay, letter, cover_letter, resume, plain)
        **kwargs: Format-specific parameters

    Returns:
        Formatted text
    """
    formatter = TextFormatter()
    return formatter.format_text(text, format_type, **kwargs)
