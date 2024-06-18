import { Component } from "react";

interface User {
  name: string;
  age: number;
}

interface UserSerachProps {
  users: User[];
}

interface UserSearchState {
  name: string;
  user: User | undefined;
}

class UserSearch extends Component<UserSerachProps> {
  state: UserSearchState = {
    name: "",
    user: undefined,
  };

  onClick = () => {
    const foundUser = this.props.users.find((user) => {
      return user.name === this.state.name;
    });
    this.setState({ user: foundUser });
  };

  render() {
    return (
      <div>
        User Search
        <input
          value={this.state.name}
          onChange={(e) => this.setState({ name: e.target.value })}
        />
        <button onClick={this.onClick}>Find User</button>
        <div>{this.state.user && this.state.user?.name}</div>
        <div>{this.state.user && this.state.user?.age}</div>
      </div>
    );
  }
}

export default UserSearch;
