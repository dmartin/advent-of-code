use aoc_runner_derive::aoc;
use itertools::Itertools;

type Crate = char;
type Stack = Vec<char>;

fn parse_stacks(input: &str) -> Vec<Stack> {
    let mut input = input.lines().rev();
    let count: i32 = input
        .next()
        .unwrap()
        .split_whitespace()
        .next_back()
        .unwrap()
        .parse()
        .unwrap();
    let mut stacks: Vec<Stack> = Vec::new();
    for _ in 0..count {
        stacks.push(Vec::new());
    }
    for line in input {
        for (i, mut chunk) in line.chars().chunks(4).into_iter().enumerate() {
            let c: Crate = chunk.nth(1).unwrap();
            if c != ' ' {
                stacks[i].push(c);
            }
        }
    }
    stacks
}

trait StackExt {
    fn move_crates(&mut self, amount: usize, from_idx: usize, to_idx: usize);
    fn move_crates_as_chunk(&mut self, amount: usize, from_idx: usize, to_idx: usize);
}

impl StackExt for Vec<Stack> {
    fn move_crates(&mut self, amount: usize, from_idx: usize, to_idx: usize) {
        for _ in 0..amount {
            let c: Crate = self[(from_idx as usize) - 1].pop().unwrap();
            self[(to_idx as usize) - 1].push(c);
        }
    }

    fn move_crates_as_chunk(&mut self, amount: usize, from_idx: usize, to_idx: usize) {
        let mut from_stack = std::mem::take(&mut self[(from_idx as usize) - 1]);
        let mut to_stack = std::mem::take(&mut (self[(to_idx as usize) - 1]));
        to_stack.extend(from_stack.drain(from_stack.len() - amount..from_stack.len()));
        self[(from_idx as usize) - 1] = from_stack;
        self[(to_idx as usize) - 1] = to_stack;
    }
}

#[aoc(day5, part1)]
fn part1(input: &str) -> String {
    let (stack_input, moves) = input.split_once("\n\n").unwrap();
    let mut stacks = parse_stacks(stack_input);
    for line in moves.lines() {
        let mut line = line.split_whitespace();
        let _ = line.next();
        let amount: usize = line.next().unwrap().parse().unwrap();
        let _ = line.next();
        let from: usize = line.next().unwrap().parse().unwrap();
        let _ = line.next();
        let to: usize = line.next().unwrap().parse().unwrap();
        stacks.move_crates(amount, from, to);
    }
    let mut result = String::new();
    for stack in stacks {
        result.push(*stack.last().unwrap());
    }
    result
}

#[aoc(day5, part2)]
fn part2(input: &str) -> String {
    let (stack_input, moves) = input.split_once("\n\n").unwrap();
    let mut stacks = parse_stacks(stack_input);
    for line in moves.lines() {
        let mut line = line.split_whitespace();
        let _ = line.next();
        let amount: usize = line.next().unwrap().parse().unwrap();
        let _ = line.next();
        let from: usize = line.next().unwrap().parse().unwrap();
        let _ = line.next();
        let to: usize = line.next().unwrap().parse().unwrap();
        stacks.move_crates_as_chunk(amount, from, to);
    }
    let mut result = String::new();
    for stack in stacks {
        result.push(*stack.last().unwrap());
    }
    result
}
