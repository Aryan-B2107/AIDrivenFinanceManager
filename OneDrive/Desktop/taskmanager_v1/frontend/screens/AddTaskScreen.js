import React, { useState } from 'react';
import { View, TextInput, Button } from 'react-native';
import axios from '../api/axiosInstance';

export default function AddTaskScreen({ navigation }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const addTask = () => {
    axios.post('tasks/', { title, description })
      .then(() => navigation.goBack())
      .catch(error => console.error('Error adding task:', error));
  };

  return (
    <View style={{ padding: 16 }}>
      <TextInput
        placeholder="Title"
        value={title}
        onChangeText={setTitle}
        style={{ borderBottomWidth: 1, marginBottom: 12 }}
      />
      <TextInput
        placeholder="Description"
        value={description}
        onChangeText={setDescription}
        style={{ borderBottomWidth: 1, marginBottom: 12 }}
      />
      <Button title="Save Task" onPress={addTask} />
    </View>
  );
}
