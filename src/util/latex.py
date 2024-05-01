import pandas as pd

def excel_to_latex_table(excel_path, caption, label, output_file_path, is_global=False):
    """
    Reads an Excel file and converts the dataframe to LaTeX.

    :param excel_path: The path of the Excel file.
    :type excel_path: str
    :param caption: The caption for the LaTeX table.
    :type caption: str
    :param label: The label for the LaTeX table.
    :type label: str
    :return: The LaTeX code for the table.
    :rtype: str
    """
    # Read the Excel file
    df = pd.read_excel(excel_path)

    # Create the LaTeX table
    table = "\\begin{footnotesize}\n"
    table += "\\begin{longtable}{p{4cm}p{2.2cm}p{2.2cm}p{2.2cm}}\n"
    table += f"\\caption{{{caption}}} \\label{{{label}}} \\\\\n"
    table += "\\toprule\n"
    table += "Variables \\newline $(\\mu \\pm \\sigma)$ & Total Population \\newline (n=184674) & Train dataset \\newline (n=147739) & Test Dataset \\newline (n=36935) \\\\ \\midrule %\\hline\n"
    table += "\\endfirsthead\n"
    table += "\\multicolumn{4}{@{}c}{\\tablename\\ \\thetable{} -- continued from previous page} \\\\\n"
    table += "\\toprule\n"
    table += "Variables \\newline $(\\mu \\pm \\sigma)$ & Total Population\\newline (n=184674) & Train dataset \\newline (n=147739) & Test Dataset \\newline (n=36935) \\\\ \\midrule %\\hline\n"
    table += "\\endhead\n"
    table += "\\midrule \\multicolumn{4}{l}{{Continued on next page}} \\\\ \\midrule\n"
    table += "\\endfoot\n"
    table += "% \\hline \\hline\n"
    table += "\\endlastfoot\n"

    if is_global:
        # Add the rows to the table
        for _, row in df.iterrows():
            table += "  " + " & ".join([str(cell) for cell in row.values]) + " \\\\\n"
    else:
        # Add the rows to the table
        for _, row in df.drop('Shape', axis=1).iterrows():
            table += "  " + " & ".join([str(cell) for cell in row.values]) + " \\\\\n"


    # Add the bottom rule
    table += "  \\botrule\n"

    # Close the table
    table += "\\end{longtable}\n"
    table += "\\end{footnotesize}\n"

    # Write the table to the output file
    with open(output_file_path, 'w') as f:
        f.write(table)

    return table
