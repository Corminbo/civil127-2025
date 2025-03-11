from cal import Cal

c = Cal()
c.year(2025)
c.month("jan")
c.week_start("sun")
c.print()

c = Cal()
c.month("feb")
c.year(2025)
c.print()

c = Cal()
c.month("aug")
c.year(2025)
c.week_start("thu")
c.print()

