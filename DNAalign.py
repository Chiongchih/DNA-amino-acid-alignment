import time
import re
import string

starts = time.clock()

def s(si_, sj_):
    if qu[si_] == seq2[sj_]:
        return 2
    else:
        return -1


def alignment(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    g = -3
    matrix = []
    for i in range(0, m):
        tmp = []
        for j in range(0, n):
            tmp.append(0)
        matrix.append(tmp)
    for k in range(0, m):
        matrix[k][0] = k * g
    for h in range(0, n):
        matrix[0][h] = h * g
    for t in range(1, m):
        for f in range(1, n):
            matrix[t][f] = max(matrix[t - 1][f] + g, matrix[t - 1][f - 1] + s(t, f),
                                     matrix[t][f - 1] + g)
    a1 = [seq1[m - 1]]
    a2 = [seq2[n - 1]]
    while m > 1 and n > 1:
        if max(matrix[m - 1][n - 2], matrix[m - 2][n - 2], matrix[m - 2][n - 1]) == matrix[m - 2][n - 2]:
            m -= 1
            n -= 1
            a1.append(seq1[m - 1])
            a2.append(seq2[n - 1])
        elif max(matrix[m - 1][n - 2], matrix[m - 2][n - 2], matrix[m - 2][n - 1]) == matrix[m - 1][n - 2]:
            n -= 1
            a1.append('-')
            a2.append(seq2[n - 1])
        else:
            m -= 1
            a1.append(seq1[m - 1])
            a2.append('-')
    a1.reverse()
    a2.reverse()
    b1 = string.join(a1, '')
    b2 = string.join(a2, '')
    score = 0
    for k in range(0, len(b1)):
        if b1[k] == b2[k]:
            score += 1
    score = float(score) / len(b2)
    show(b1,b2)
    return score

def show(seq1,seq2):
    le = 40
    while len(seq1)-le>=0:
        print 'sequence1:',
        for code in list(seq1)[le-40:le]:
            print code,
        print "\n",
        print '          ',
        for gene in range(le-40, le):
            if seq1[gene]==seq2[gene]:
                print '|',
            else:
                print  ' ',
        print "\n",
        print 'sequence2:',
        for codes in list(seq2)[le-40:le]:
            print codes,
        print "\n",
        le +=40

    if len(seq1)>le-40:
        print 'sequence1:',
        for t in list(seq1)[le-40:len(seq1)]:
                print t,
        print "\n",
        print '          ',
        for dd in range(le-40, len(seq1)):
            if seq1[dd] == seq2[dd]:
                print '|',
            else:
                print ' ',
        print "\n",
        print 'sequence2:',
        for b in list(seq2)[le-40:len(seq2)]:
                print b,
        print "\n"
        

seq1='ATCCGCTCAGGCACCAAAAAACTGCTGCTGCTGCTGCTGCAAAAAAATTTTTGTTTTGGGCGTCGTCCTG'
seq2='ATCGGCTGAGGCAAAAAAAACTGCTGCTGCTGCTGCTGCAAATAAATTTTTTTTTTGGGGGTCGTCCTC'
alignment(seq1, seq2)
end = time.clock()
print "using time: %fs" % (end - starts)

