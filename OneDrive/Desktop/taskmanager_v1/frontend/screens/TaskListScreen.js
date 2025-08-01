import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Button } from 'react-native';
import axios from '../api/axiosInstance';

export default function TaskListScreen({ navigation }) {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get('tasks/')
      .then(response => setTasks(response.data))
      .catch(error => console.error('Error fetching tasks:', error));
  }, []);

  return (
    <View style={{ padding: 16 }}>
      <Button
        title="Add Task"
        onPress={() => navigation.navigate('AddTask')}
      />
      <FlatList
        data={tasks}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => (
          <View style={{ marginVertical: 8 }}>
            <Text style={{ fontWeight: 'bold' }}>{item.title}</Text>
            <Text>{item.description}</Text>
          </View>
        )}
      />
    </View>
  );
}
