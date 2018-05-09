

def read_fp_lib_table(filename):
    return read_lib_table (filename, "fp")

def read_sym_lib_table(filename):
    return read_lib_table (filename, "sym")

def read_lib_table(filename, atype):
    fr = open(filename, "r")
    d = fr.read()
    fr.close()

    d = d.strip()
    table_tag = "(" + atype + "_lib_table"

    d = d[d.find(table_tag) + len(table_tag):]

    masterLineItemArray = d.splitlines()
    libs = []
    for d in masterLineItemArray:

        
        d = d.strip()
        lineItemArray = d.splitlines()
        for lineItem in lineItemArray:
            lib = {}
            lineItem = lineItem.strip()
            lineItem = lineItem.replace("(lib","")
            lineItem = lineItem.strip()
            lineItem = lineItem.strip()

            parseItems = lineItem.split(")(")

            for tok in parseItems:             
                
                tok = tok.strip("(")
                tok = tok.strip("))")

                if tok != "":

                    tokens = tok.split(None, 1)

                    key = tokens[0]

                    if len(tokens)>1 :
                        val = tokens[1]
                        val = val.strip("\"")
                        val = val.strip("\"")
                        val = val.strip("\"")
                    else:
                        val = None
                    lib[key] = val

                    print("Val: " + lib[key])

            if len(lib) >= 1:
                libs.append(lib)
    
    return libs

def write_fp_lib_table(filename, libs):
    write_lib_table (filename, "fp", libs)

def write_sym_lib_table(filename, libs):
    write_lib_table (filename, "sym", libs)

def write_lib_table(filename, atype, libs):
    fw = open(filename, "w")

    if atype == "fp":
        fw.write("(fp_lib_table\n")
    else:
        fw.write("(sym_lib_table\n")

    for lib in libs:
        line = "(lib (name \"%s\")(type \"%s\")(uri \"%s\")(options \"%s\")(descr \"%s\")" % (lib['name'].strip("\""), lib['type'].strip("\""), lib['uri'].strip("\""), lib['options'].strip("\""), lib['descr'].strip("\""))
        if 'disabled' in lib:
            line += "(disabled)"
        line += ")"
        fw.write("  %s\n" % line)

    fw.write(")\n")
    fw.close()

