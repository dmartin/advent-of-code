use aoc_runner_derive::aoc;

struct SectionAssignment {
    pub start: i32,
    pub end: i32,
}

impl From<&str> for SectionAssignment {
    fn from(s: &str) -> Self {
        let (start, end) = s.split_once('-').unwrap();
        Self {
            start: start.parse().unwrap(),
            end: end.parse().unwrap(),
        }
    }
}

impl SectionAssignment {
    fn overlaps(&self, other: &SectionAssignment) -> bool {
        self.start.max(other.start) <= self.end.min(other.end)
    }
}

#[aoc(day4, part1)]
fn part1(input: &str) -> i32 {
    input.lines().fold(0, |acc, line| {
        let (assignment1, assignment2) = line.split_once(',').unwrap();
        let (assignment1, assignment2): (SectionAssignment, SectionAssignment) =
            (assignment1.into(), assignment2.into());
        if (assignment1.start >= assignment2.start && assignment1.end <= assignment2.end)
            || (assignment2.start >= assignment1.start && assignment2.end <= assignment1.end)
        {
            acc + 1
        } else {
            acc
        }
    })
}

#[aoc(day4, part2)]
fn part2(input: &str) -> i32 {
    input.lines().fold(0, |acc, line| {
        let (assignment1, assignment2) = line.split_once(',').unwrap();
        let (assignment1, assignment2): (SectionAssignment, SectionAssignment) =
            (assignment1.into(), assignment2.into());
        if assignment1.overlaps(&assignment2) {
            acc + 1
        } else {
            acc
        }
    })
}
