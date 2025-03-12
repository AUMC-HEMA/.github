from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("Amsterdam UMC Hematology Department", guide_style="bold bright_black")

package_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
package_tree.add("[bold link=https://github.com/AUMC-HEMA/MSGMM]MSGMM[/] - [bright_black]Multi-sample Gaussian mixture models")
package_tree.add("[bold link=https://github.com/AUMC-HEMA/MSGMM]CytoTools[/] - [bright_black]Internal R utilities package for cytometry data")

manuscript_tree = tree.add("🔬 Manuscripts", guide_style="bright_black")
manuscript_tree.add("[bold link=https://github.com/AUMC-HEMA/imputation-manuscript]imputation-manuscript[/] - [bright_black]Imputation of cytometry data (Mocking et al., 2023)")
manuscript_tree.add("[bold link=https://github.com/AUMC-HEMA/cMRD-manuscript]cMRD-manuscript[/] - [bright_black]Computational MRD assessment in AML (Mocking et al., 2024)")
manuscript_tree.add("[bold link=https://github.com/AUMC-HEMA/cMRD-manuscript]cMRD-review[/] - [bright_black]Review of computational MRD assessment in AML (Mocking et al., 2025)")

contributor_tree = tree.add("👨‍💻 Contributors", guide_style="bright_black")
postdoc_tree = contributor_tree.add("👨‍💻 Postdoctoral scientists", guide_style="bright_black")
postdoc_tree.add("[bold link=https://researchinformation.amsterdamumc.org/en/persons/costa-bachas]Costa Bachas[/] - [bright_black]Postdoc")

phd_tree = contributor_tree.add("👨‍💻 PhD students", guide_style="bright_black")
phd_tree.add("[bold link=https://timmocking.github.io]Tim Mocking[/] - [bright_black]Computational analysis of myeloid malignancies")
phd_tree.add("[bold link=https://researchinformation.amsterdamumc.org/en/persons/tom-reuvekamp]Tom Reuvekamp[/] - [bright_black]Therapy dependent leukemic stem cell dynamics in acute myeloid leukemia")
phd_tree.add("[bold link=https://researchinformation.amsterdamumc.org/en/persons/lukas-haaksma]Lukas Haaksma[/] - [bright_black]Advanced measurable residual disease modeling in acute myeloid leukemia")
phd_tree.add("[bold link=https://researchinformation.amsterdamumc.org/en/persons/kasper-croese]Kasper Croese[/] - [bright_black]Computational analysis of myeloid malignancies")
phd_tree.add("[bold link=https://researchinformation.amsterdamumc.org/en/persons/nils-evander]Nils Evander[/] - [bright_black]Drug resistance modeling in acute leukemia")

intern_tree = contributor_tree.add("👨‍💻 Students", guide_style="bright_black")
intern_tree.add("Marry Lin - [bright_black]Intern MSc. Biomedical Sciences")
intern_tree.add("Felix Zwolle - [bright_black]Intern MSc. Bioinformatics")

alumni_tree = contributor_tree.add("👨‍💻 Alumni", guide_style="bright_black")
alumni_tree.add("Eirini Papavasileiou - [bright_black]Intern MSc. Bioinformatics")
alumni_tree.add("Lok Lam Ngai - [bright_black]PhD student")
alumni_tree.add("Jesse Tettero - [bright_black] PhD student")
alumni_tree.add("Philip Rutten - [bright_black]Postdoc")
alumni_tree.add("Dana Allen - [bright_black]Intern MSc. Bioinformatics")
alumni_tree.add("Yejin Park - [bright_black]Intern MSc. Bioinformatics")

console.print(tree)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
