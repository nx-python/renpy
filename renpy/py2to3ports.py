from lib2to3.refactor import RefactoringTool, get_fixers_from_package


def FixParens(codeContents):
    refactoring_tool = RefactoringTool(fixer_names=['lib2to3.fixes.fix_paren'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixUrllib(codeContents):
    refactoring_tool = RefactoringTool(fixer_names=['lib2to3.fixes.fix_urllib'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixUnicode(codeContents):
    refactoring_tool = RefactoringTool(fixer_names=['lib2to3.fixes.fix_unicode'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixExecStatment(codeContents):
    refactoring_tool = RefactoringTool(fixer_names=['lib2to3.fixes.fix_exec'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)
