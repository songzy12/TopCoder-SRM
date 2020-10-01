# https://community.topcoder.com/stat?c=round_overview&er=5&rd=18266


class BicycleLock:
    def makeDistinct(self, dials):
        def find_dail(visited, dial):
            move = ''
            while dial in visited:
                dial = (dial + 1) % 10
                move += '+'
            return move, dial

        ans = ''
        visited = set()
        for dial in dials:
            if dial not in visited:
                visited.add(dial)
            else:
                move, target = find_dail(visited, dial)
                ans += move
                visited.add(target)
            ans += ">"
        return ans.rstrip(">")
