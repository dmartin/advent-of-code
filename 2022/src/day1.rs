use aoc_runner_derive::aoc;

// Store a running caloric total (index 0) plus the highest observed calories/elf (index 1+),
// updating the highest-observed slots when a blank line is encountered.

// Optimizing for space complexity rather than time. Suitable for inputs of arbitrary size.

#[aoc(day1, part1)]
fn part1(input: &str) -> i32 {
    input
        .lines()
        .fold((0, 0), |mut acc, x| {
            if x.is_empty() {
                acc.1 = std::cmp::max(acc.0, acc.1);
                acc.0 = 0;
            } else {
                let calories: i32 = x.parse().unwrap();
                acc.0 += calories;
            }
            acc
        })
        .1
}

#[aoc(day1, part2)]
fn part2(input: &str) -> i32 {
    let acc = input.lines().fold((0, 0, 0, 0), |mut acc, x| {
        if x.is_empty() {
            acc.1 = std::cmp::max(acc.0, acc.1);
            if acc.1 > acc.2 {
                std::mem::swap(&mut acc.1, &mut acc.2);
            }
            if acc.2 > acc.3 {
                std::mem::swap(&mut acc.2, &mut acc.3);
            }
            acc.0 = 0;
        } else {
            let calories: i32 = x.parse().unwrap();
            acc.0 += calories;
        }
        acc
    });
    acc.1 + acc.2 + acc.3
}
