class SelfDescFind:
    def construct(self, digits):
        def get_key(i):
            return "".join(sorted(list(set(str(i)))))
        def check(i):
            i = str(i)
            if len(i) % 2 != 0:
                return False
        
            a = [int(i[t]) for t in range(0, len(i), 2)]
            b = [i[t] for t in range(1, len(i), 2)]
            if len(set(b)) != len(b):
                return False

            if len(set(b)) != len(set(str(i))):
                return False

            for index, c in enumerate(b):
                if i.count(c) != a[index]:
                    return False
            return True
            
        def compute_m():
            m = {}
            for i in range(10**20):
                if i % 10**4 == 0:
                    print(i)
                key = get_key(i)
                if key in m:
                    continue
                if check(i):
                    m[key] = i
            import io, json
            with io.open('m.json', 'w', encoding='utf8') as f:
                f.write(json.dumps(m, indent=2))
            return m

        m = compute_m()
        
        return m.get("".join(map(str, digits)), "")

for digits in [(1), (2), (0,1,3,4)]:
    print(SelfDescFind().construct(digits))