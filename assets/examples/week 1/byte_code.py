import dis, inspect
import example_module

for name, f in inspect.getmembers(example_module, inspect.isfunction):
    source = ''.join([str(l) for l in inspect.getsourcelines(f)[0]])
    print(f"\n\n```python\n{source}\n```")
    code = dis.Bytecode(f)
    print(f'```plaintext\n \tOPCODE\tOPNAME        \t\tARG\tARGVAL')
    for op in code:
        print(f'{op.offset}\t{op.opcode}\t{op.opname.ljust(20)}\t{op.arg}\t{op.argval}')
    print("```")