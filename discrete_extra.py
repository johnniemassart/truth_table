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
       
       
            
    # # TRUTH TABLE FOR PROPOSITIONAL VARIABLES
    def truth_setup(self):
        sth = []
        var_count = self.var_count()
        var_count_rows = 2**var_count
        for i in range(var_count_rows):
            nest_sth = []
            iteration_count = 0
            var_count_rows_copy = var_count_rows
            half = var_count_rows/2
            for j in range(var_count):
                if j == iteration_count and i % var_count_rows_copy < half:
                    nest_sth.append(1)
                elif j == iteration_count and i % var_count_rows_copy >= half:
                    nest_sth.append(0)
                iteration_count += 1
                var_count_rows_copy /= 2
                half /= 2
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
    
    
    
    # TRUTH COLUMN FOR LEFT HAND SIDE (EQUIVALENT (==) SIGN)
    def truth_lhs(self):
        sth = self.truth_setup()
        for i in range(len(sth)):
            sum = 0
            inner_counter = 0
            nest_sth = []
            for j in sth[i]:
                sum += j
                inner_counter += 1
                if inner_counter == len(sth[i]):
                    if sum == len(sth[i]) or sum == 0:
                        sum = 1
                        nest_sth.append(sum)
                    else:
                        sum = 0
                        nest_sth.append(sum)
            sth[i].append(nest_sth)
        return sth   
    
    
    
    # LEFT HAND SIDE MATRIX OUTPUT
    def lhs_output(self):
        print(f"Truth Table - Left Hand Side")
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
    
    
    
    # TRUTH COLUMN FOR RIGHT HAND SIDE, EQUIVALENCE (==) SIGN
    def truth_rhs_equiv(self):
        sth = self.truth_setup()
        equiv = []
        for i in range(len(sth)):
            sum = 0
            inner_counter = 0
            first = 0
            second = 1
            nest_sth = []
            while inner_counter < len(sth[i]):
                if inner_counter == first:
                    sum += sth[i][inner_counter]
                    inner_counter += 1
                elif inner_counter == second:
                    sum += sth[i][inner_counter]
                    if sum != 1:
                        nest_sth.append(1)
                    elif sum == 1:
                        nest_sth.append(0)
                    first += 1
                    second += 1
                    sum = 0
                    inner_counter = first
            equiv.append(nest_sth)
        return equiv
        
        
         
    # TRUTH COLUMN FOR RIGHT HAND SIDE, AND (^) SIGN
    def truth_rhs_and(self):
        sth = self.truth_rhs_equiv()
        and_ = []
        for i in range(len(sth)):
            sum = 0
            nest_sth = []
            for j in range(len(sth[i])):
                sum += sth[i][j]
                if j == len(sth[i]) - 1:
                    if sum == len(sth[i]):
                        nest_sth.append(1)
                    else:
                        nest_sth.append(0)
            and_.append(nest_sth)
        return and_
    
    
    
    # APPEND EQUIVALENCE (==), AND (^) TO RHS TRUTH TABLE
    def rhs_appended(self):
        sth = self.truth_setup()
        equiv = self.truth_rhs_equiv()
        and_ = self.truth_rhs_and()
        for i in range(len(sth)):
            sth[i].append(equiv[i])
            sth[i].append(and_[i])
        return sth
        
        
    
    # RIGHT HAND SIDE MATRIX OUTPUT
    def rhs_output(self):
        print(f"Truth Table - Right Hand Side")
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
        content = self.rhs_appended()
        for i in content:
            print(i)
            
    
    
    # COMPLETE OUTPUT
    def complete_output(self):
        self.lhs_output()
        print()
        self.rhs_output()
        
        

   
eq = "(p == q == r) === (p == q) ^ (q == r)"
# eq = "(p == q == r == x) === (p == q) ^ (q == r) ^ (r == x)"
# eq = "(p == q == r == x == y) === (p == q) ^ (q == r) ^ (r == x) ^ (x == y)"


my = Eq_Truth_Table(eq)
    

my.complete_output()
