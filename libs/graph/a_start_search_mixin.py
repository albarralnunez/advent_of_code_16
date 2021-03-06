from libs.priority_queue import PriorityQueue


class AStarSearchMixin(object):
    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.push(start, 0)
        came_from = {start: None}
        cost_so_far = {start: 0}
        while len(frontier) != 0:
            current = frontier.pop()
            if current == goal:
                break
            for neighbour in current.neighbors:
                new_cost = (cost_so_far[current] +
                            self.movement_cost(current, neighbour))
                if (neighbour not in cost_so_far or
                            new_cost < cost_so_far[neighbour]):
                    cost_so_far[neighbour] = new_cost
                    priority = new_cost + self.heuristic(goal, neighbour)
                    frontier.push(neighbour, priority)
                    came_from[neighbour] = current
        return came_from, cost_so_far
