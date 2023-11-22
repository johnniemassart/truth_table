class Eq_Truth_Table:
    
    #USER INPUT
    def __init__(self, eq):
        self.eq = eq
    
    
    
    # DETERMINE VARIABLE COUNT FROM EQUATION
    def var_count(self):
        eq_set = set(self.eq)
        counting = 0
        for i in eq_set:
            if i.isalpha():
                counting += 1
        return counting
    
    
    
    # DETERMINE PROPOSITIONAL VARIABLES FROM EQUATION
    def prop_vars(self):
        eq_set = set(self.eq)
        prop_vars = []
        for i in eq_set:
            if i.isalpha():
                prop_vars.append(i)
        return sorted(prop_vars)
       
       
            
    # TRUTH TABLE FOR PROPOSITIONAL VARIABLES
    def truth_setup(self):
        sth = []
        vars = self.var_count()
        prop_vars_rows = 2**vars
        for i in range(prop_vars_rows):
            nest_sth = []
            for j in range(vars):
                #
                if j == 0 and i < prop_vars_rows/2:
                    nest_sth.append(1)
                elif j == 0 and i >= prop_vars_rows/2:
                    nest_sth.append(0)
                #
                elif (j == 1 and i % (prop_vars_rows/2) < (prop_vars_rows/2)/2):
                    nest_sth.append(1)
                elif (j == 1 and i % (prop_vars_rows/2) >= (prop_vars_rows/2)/2):
                    nest_sth.append(0)
                #
                elif j == 2 and i % 2 == 0:
                    nest_sth.append(1)
                elif j == 2 and i % 2 != 0:
                    nest_sth.append(0)
            sth.append(nest_sth)
        return sth
    
    
    
    # EQUATION LIST
    def equation_list(self):
        eq_list = list(self.eq)
        for i in eq_list:
            if i == ' ':
                eq_list.remove(i)
        eq_list_split = []
        sth = ""
        counter = 0
        for i in range(len(eq_list)):
            sth += eq_list[i]
            if sth == "===" or sth == "^":
                eq_list_split.append(sth)
                sth = ""
            if eq_list[i] == "(":
                sth = "" + eq_list[i]
                counter += 1
            if eq_list[i] == ")" and counter > 0:
                eq_list_split.append(sth)
                sth = ""
                counter = 0
        return eq_list_split
    
    
    
    # DETERMINE LEFT EQUATION
    def left_eq(self):
        equation_list = self.equation_list()
        left_eq_list = []
        for i in equation_list:
            if i == "===":
                break
            else:
                left_eq_list.append(i)
        return left_eq_list
    
    
    
    # DETERMINE RIGHT EQUATION
    def right_eq(self):
        equation_list = self.equation_list()
        right_eq_list = []
        counter = 0
        for i in equation_list:
            if i == "===":
                break
            counter += 1
        for i in range(len(equation_list)):
            if i > counter:
                right_eq_list.append(equation_list[i])
        return right_eq_list
            
    
    
    # TRUTH COLUMN FOR LEFT HAND SIDE (EQUIVALENT (==) SIGN)
    def truth_lhs(self):
        sth = self.truth_setup()
        for i in range(len(sth)):
            sum = 0
            inner_counter = 0
            for j in sth[i]:
                sum += j
                inner_counter += 1
                if inner_counter == len(sth[i]):
                    if sum == len(sth[i]) or sum == 0:
                        sum = 1
                    else:
                        sum = 0    
            sth[i].append(sum)
        return sth
    
    
    
    # LEFT HAND SIDE MATRIX OUTPUT
    def lhs_output(self):
        print(f"TRUTH TABLE, LEFT HAND SIDE OF EQUATION")
        header = self.prop_vars()
        for i in range(len(header)):
            print(f"Column {i+1}: {header[i]}")
        eq_str = ""
        for i in self.left_eq():
            eq_str += i
        print(f"Column {len(header)+1}: {eq_str}")
        lhs = self.truth_lhs()
        for i in lhs:
            print(i)
    
    
    
    # TRUTH COLUMNS FOR RIGHT HAND SIDE (EQUIVALENT (==), AND (^) SIGN)
    def right_equation(self):
        # right_eq_list = self.right_eq()
        sth = self.truth_setup()
        for i in range(len(sth)):
            pq_sum = 0
            qr_sum = 0
            inner_counter = 0
            for j in sth[i]:
                inner_counter += 1
                if inner_counter == 1 or inner_counter == 2:
                    pq_sum += j
                if inner_counter == 2 or inner_counter == 3:
                    qr_sum += j
                if inner_counter == len(sth[i]):
                    if pq_sum != 1:
                        pq_sum = 1
                    elif pq_sum == 1:
                        pq_sum = 0
                    if qr_sum != 1:
                        qr_sum = 1
                    elif qr_sum == 1:
                        qr_sum = 0
            sth[i].append(pq_sum)
            sth[i].append(qr_sum)
        for i in range(len(sth)):
            pq_and_qr = 0
            inner = 0
            for j in sth[i]:
                inner += 1
                if inner == 4 or inner == 5:
                    pq_and_qr += j
                if inner == len(sth[i]):
                    if pq_and_qr == 2:
                        pq_and_qr = 1
                    else:
                        pq_and_qr = 0
            sth[i].append(pq_and_qr)
        return sth
            
        
    
    # RIGHT HAND SIDE MATRIX OUTPUT
    def rhs_output(self):
        print(f"TRUTH TABLE, RIGHT HAND SIDE OF EQUATION")
        header = self.prop_vars()
        for i in range(len(header)):
            print(f"Column {i+1}: {header[i]}")
        right_eq = self.right_eq()
        counter = len(header) + 1
        right_total = ""
        for i in range(len(right_eq)):
            right_total += right_eq[i]
            if right_eq[i] == "^":
                continue
            print(f"Column {counter}: {right_eq[i]}")
            counter += 1
        print(f"Column {counter}: {right_total}")
        content = self.right_equation()
        for i in content:
            print(i)
            
    
    
    # COMPLETE OUTPUT
    def complete_output(self):
        self.lhs_output()
        print()
        self.rhs_output()
        
        

   
eq = "(p == q == r) === (p == q) ^ (q == r)"


my = Eq_Truth_Table(eq)


my.complete_output()