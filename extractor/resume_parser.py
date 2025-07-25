from typing import List, Dict

class ResumeParser:
    def __init__(self, resume_text: str):
        self.resume_text = resume_text
        self.parsed_data = {}

    def parse(self) -> Dict[str, str]:
        self._extract_personal_info()
        self._extract_experience()
        self._extract_education()
        return self.parsed_data

    def _extract_personal_info(self):
        # Example extraction logic for personal information
        lines = self.resume_text.splitlines()
        self.parsed_data['name'] = lines[0]  # Assuming the first line is the name
        self.parsed_data['email'] = self._extract_email(lines)

    def _extract_email(self, lines: List[str]) -> str:
        for line in lines:
            if "@" in line:
                return line.strip()
        return ""

    def _extract_experience(self):
        # Example extraction logic for experience
        experience_section = self._get_section("Experience")
        self.parsed_data['experience'] = experience_section

    def _extract_education(self):
        # Example extraction logic for education
        education_section = self._get_section("Education")
        self.parsed_data['education'] = education_section

    def _get_section(self, section_title: str) -> str:
        # Logic to extract a section from the resume text
        section_lines = []
        lines = self.resume_text.splitlines()
        in_section = False

        for line in lines:
            if line.strip() == section_title:
                in_section = True
                continue
            if in_section and line.strip() == "":
                break
            if in_section:
                section_lines.append(line.strip())

        return "\n".join(section_lines) if section_lines else "Not provided"