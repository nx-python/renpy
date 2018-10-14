

def FixParens(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_paren'])
    try:
        node3 = refactoring_tool.refactor_string(codeContents, 'script')
        return str(node3)
    except:
        return codeContents


def FixUrllib(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_urllib'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixUnicode(codeContents,_RefactoringTool):
    try:
        refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_unicode'])
        node3 = refactoring_tool.refactor_string(codeContents, 'script')
        return str(node3)
    except:
        return codeContents


def FixExecStatment(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_exec'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixNumLiterals(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_numliterals'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixPrintStatement(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_print'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixExceptStatement(codeContents,_RefactoringTool):
    try:
        refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_except'])
        node3 = refactoring_tool.refactor_string(codeContents, 'script')
        return str(node3)
    except:
        return codeContents


def FixXrange(codeContents,_RefactoringTool):
    try:
        refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_xrange'])
        node3 = refactoring_tool.refactor_string(codeContents, 'script')
        return str(node3)
    except:
        return codeContents


def FixBasestring(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_basestring'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixImports(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_imports'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixDict(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_dict'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixFunctionAttribs(codeContents,_RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_funcattrs'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixImportsRelativity(codeContents,_RefactoringTool, FileName):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_import'])
    node3 = refactoring_tool.refactor_string(codeContents, FileName)
    return str(node3)


def FixRaise(codeContents, _RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_raise'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def FixThrow(codeContents, _RefactoringTool):
    refactoring_tool = _RefactoringTool(fixer_names=['lib2to3.fixes.fix_throw'])
    node3 = refactoring_tool.refactor_string(codeContents, 'script')
    return str(node3)


def GenericReplacements(codeContents):
    import re
    inner_code = codeContents
    if "b\"" in inner_code:
        inner_code = re.sub(r'os\.environ\.get\(b', "os.environ.get(", inner_code)
        inner_code = re.sub(r'os.environ.pop\(b', "os.environ.pop(", inner_code)
    if "basestring)" in inner_code:
        inner_code = re.sub(r"basestring\)", "str)", inner_code)
    if " file(" in inner_code:
        inner_code = re.sub(r" file\(", " open(", inner_code)
    if "unicode(" in inner_code:
        inner_code = re.sub(r" unicode\("," str(", inner_code)
    if "\"/usr/bin/python\"" in inner_code:
        inner_code = re.sub(r"\"/usr/bin/python\"", "sys.executable", inner_code)
    return inner_code


def PerformFixes(codeContents, Filename):
    import re
    from lib2to3.refactor import RefactoringTool as _RefactoringTool
    inner_code = codeContents
    inner_code = GenericReplacements(inner_code)
    if re.search(r"(for \w* in )", inner_code, re.IGNORECASE | re.MULTILINE):
        inner_code = FixParens(inner_code,_RefactoringTool)
    if re.search(r"(= 0[0-9]+)", inner_code, re.IGNORECASE | re.MULTILINE):
        inner_code = FixNumLiterals(inner_code,_RefactoringTool)
    if re.search(r"(ur\"|ur\')", inner_code, re.IGNORECASE | re.MULTILINE):
        inner_code = FixUnicode(inner_code,_RefactoringTool)
    if "urllib" in inner_code:
        inner_code = FixUrllib(inner_code,_RefactoringTool)
    if "unicode(" in inner_code:
        inner_code = FixUnicode(inner_code,_RefactoringTool)
    if "exec " in inner_code:
        inner_code = FixExecStatment(inner_code,_RefactoringTool)
    if "print " in inner_code:
        inner_code = FixPrintStatement(inner_code,_RefactoringTool)
    if "except " in inner_code:
        inner_code = FixExceptStatement(inner_code,_RefactoringTool)
    if "xrange" in inner_code:
        inner_code = FixXrange(inner_code,_RefactoringTool)
    if "urlparse" in inner_code:
        inner_code = FixImports(inner_code,_RefactoringTool)
    if "cPickle" in inner_code:
        inner_code = FixImports(inner_code,_RefactoringTool)
    if "iteritems" in inner_code:
        inner_code = FixDict(inner_code,_RefactoringTool)
    if "func_name" in inner_code:
        inner_code = FixFunctionAttribs(inner_code,_RefactoringTool)
    if "throw(" in inner_code:
        inner_code = FixThrow(inner_code,_RefactoringTool)
    return inner_code
