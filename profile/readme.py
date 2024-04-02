from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("Amsterdam UMC Hematology Department", guide_style="bold bright_black")

package_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
package_tree.add("[bold link=https://github.com/AUMC-HEMA/MSGMM]MSGMM[/] - [bright_black]Multi-sample Gaussian mixture models")

manuscript_tree = tree.add("🔬 Manuscripts", guide_style="bright_black")
manuscript_tree.add("[bold link=https://github.com/AUMC-HEMA/imputation-manuscript]imputation-manuscript[/] - [bright_black]Imputation of cytometry data (Mocking et al., 2023)")

contributor_tree = tree.add("👨‍💻 Contributors", guide_style="bright_black")

postdoc_tree = contributor_tree.add("👨‍💻 Postdoctoral scientists", guide_style="bright_black")
postdoc_tree.add("[bold link=https://researchinformation.amsterdamumc.org/en/persons/costa-bachas]Costa Bachas[/] - [bright_black]Postdoc")
postdoc_tree.add("[bold link=https://researchinformation.amsterdamumc.org/en/persons/costa-bachas]Philip Rutten[/] - [bright_black]Postdoc")

phd_tree = contributor_tree.add("👨‍💻 PhD students", guide_style="bright_black")
phd_tree.add("[bold link=https://timmocking.github.io]Tim Mocking[/] - [bright_black]Computational analysis of myeloid malignancies")

intern_tree = contributor_tree.add("👨‍💻 Students", guide_style="bright_black")
intern_tree.add("Dana Allen - [bright_black]Intern MSc. Bioinformatics")

former_intern_tree = contributor_tree.add("👨‍💻 Former students", guide_style="bright_black")
former_intern_tree.add("Yejin Park - [bright_black]Intern MSc. Bioinformatics")

console.print(tree)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
