"""Prompt templates"""

from typing import Dict, Any
import re

class PromptTemplate:
    """Template for dynamic prompts."""
    
    def __init__(self, template: str):
        self.template = template
        self._variables = self._extract_variables()
    
    def _extract_variables(self) -> list:
        """Extract variable names from template."""
        return re.findall(r'\{(\w+)\}', self.template)
    
    def format(self, **kwargs) -> str:
        """Format template with variables."""
        return self.template.format(**kwargs)
    
    def partial(self, **kwargs) -> 'PromptTemplate':
        """Create partial template with some variables filled."""
        new_template = self.template
        for key, value in kwargs.items():
            new_template = new_template.replace(f'{{{key}}}', str(value))
        return PromptTemplate(new_template)
    
    @property
    def variables(self) -> list:
        """Get list of template variables."""
        return self._variables

# Common templates
CODE_REVIEW_TEMPLATE = PromptTemplate('''
Please review the following code:

File: {filename}
```{language}
{code}
```

Focus on:
- Code quality and best practices
- Potential bugs or issues
- Performance considerations
''')

EXPLAIN_CODE_TEMPLATE = PromptTemplate('''
Explain what this code does:

```{language}
{code}
```
''')

FIX_ERROR_TEMPLATE = PromptTemplate('''
The following error occurred:

```
{error}
```

In file: {filename}
Please suggest a fix.
''')
