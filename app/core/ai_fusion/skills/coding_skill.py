import ast

class CodingSkill:
    def execute(self, t):
        if isinstance(t, dict):
            task_name = t.get("task","coding_task")
            code_content = t.get("code","")
        else:
            task_name = str(t)
            code_content = str(t)
        if not code_content.strip():
            return {"status":"failed","task":task_name,"syntax_valid":False,"message":"No code provided."}
        try:
            ast.parse(code_content)
            return {"status":"success","task":task_name,"syntax_valid":True,"message":"Python syntax is valid."}
        except SyntaxError as e:
            return {"status":"failed","task":task_name,"syntax_valid":False,"message":f"Syntax error: {e}"}
        except Exception as e:
            return {"status":"error","task":task_name,"syntax_valid":False,"message":f"Validation error: {e}"}
