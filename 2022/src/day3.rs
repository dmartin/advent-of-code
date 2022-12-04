use itertools::Itertools;
use std::collections::HashSet;

use aoc_runner_derive::aoc;

const ASCII_UPPERCASE_A: u32 = 64;
const ASCII_LOWERCASE_A: u32 = 96;

/// Converts a character to its priority value using ASCII codepoint arithmetic
fn to_priority(c: &char) -> i32 {
    let c: u32 = (*c).into();
    if c >= ASCII_LOWERCASE_A {
        (c - ASCII_LOWERCASE_A).try_into().unwrap()
    } else {
        (c - ASCII_UPPERCASE_A + 26).try_into().unwrap()
    }
}

#[aoc(day3, part1)]
fn part1(input: &str) -> i32 {
    input
        .lines()
        .map(|x| x.split_at(&x.len() / 2))
        .map(|(x, y)| {
            let x_set: HashSet<char> = x.chars().collect();
            let y_set: HashSet<char> = y.chars().collect();
            let shared_char: &char = x_set.intersection(&y_set).next().unwrap();
            to_priority(shared_char)
        })
        .sum()
}

#[aoc(day3, part2)]
fn part2(input: &str) -> i32 {
    input
        .lines()
        .chunks(3)
        .into_iter()
        .fold(0, |mut acc, chunk| {
            let char_map = chunk.fold(HashSet::<char>::new(), |mut acc, line| {
                if acc.is_empty() {
                    acc.extend(line.chars());
                } else {
                    let line_set: HashSet<char> = line.chars().collect();
                    acc = acc.intersection(&line_set).cloned().collect()
                }
                acc
            });
            acc += to_priority(char_map.iter().next().unwrap());
            acc
        })
}
