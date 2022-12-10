
use std::collections::VecDeque;

use aoc_runner_derive::aoc;

fn first_distinct_run_index(input: &str, len: usize) -> Result<usize, String> {
    let mut seen = VecDeque::new();
    for (i, c) in input.char_indices() {
        if seen.contains(&c) {
            seen.drain(..=seen.iter().position(|e| e == &c).unwrap());
        } else if seen.len() == (len - 1) {
            return Ok(i);
        }
        seen.push_back(c);
    }
    Err("run not found".into())
}

#[aoc(day6, part1)]
fn part1(input: &str) -> i32 {
    return (first_distinct_run_index(input, 4).unwrap() + 1).try_into().unwrap();
}

#[aoc(day6, part2)]
fn part2(input: &str) -> i32 {
    return (first_distinct_run_index(input, 14).unwrap() + 1).try_into().unwrap();
}
