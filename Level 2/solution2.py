def solution(l):

    def compare(st):
        version = st.split('.')
        major = int(version[0])
        if len(version) > 1:
            minor = int(version[1])
            if len(version) > 2:
                revision = int(version[2])
            else:
                revision = -1
        else:
            minor = -1
            revision = -1

        return (major, minor, revision)

    return sorted(l, key=compare)

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))

print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))