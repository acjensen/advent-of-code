module Main

export main

function main()

  input = """1163751742
  1381373672
  2136511328
  3694931569
  7463417111
  1319128137
  1359912421
  3125421639
  1293138521
  2311944581"""
  ints = reshape(map(x -> parse(Int, x), collect(replace(input, '\n' => ""))), (10, 10))
  println(ints)

  function next_pos(curr_pos::Vector{Int}, height::Int, width::Int)::Vector{Vector{Int}}
    offsets = [[0, 1], [1, 0], [1, 1], [-1, -1]]
    neighbors = map(.+, offsets, curr_pos)
    is_within_bounds(x) = all(x .> 0) && x[1] < height && x[2] < width
    directions = findall(is_within_bounds, neighbors)
    offsets[directions], directions
  end

  # x = next_pos([1, 1], 10, 10)
  # println(x)

  function dfs()
    visited = Dict()
    deque = []
    push!(deque, ([1, 1], "down", ints[[1, 1]]))
    push!(deque, ([1, 1], "right", ints[[1, 1]]))
    while true
      curr_pos, direction, count = pop!(deque)
      if (curr_pos, direction) in keys(visited)
        if count < visited((curr_pos, direction))
          visited((curr_pos, direction)) = count
        end
      end
      visited[(curr_pos, direction)] = count
      deque = [next_pos; deque]
    end
  end

end

end

main()