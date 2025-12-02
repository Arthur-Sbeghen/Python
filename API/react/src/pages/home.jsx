"use client"

import "./home.css";
import { useState, useEffect } from 'react';
import functions from '../api/functions';

const Home = () => {
    const [tarefas, setTarefas] = useState([]);
    const [loading, setLoading] = useState(false);
    const [formData, setFormData] = useState({
        name: '',
        data: ''
    });

    useEffect(() => {
        carregarTarefas();
    }, []);

    const carregarTarefas = async () => {
        try {
            setLoading(true);
            const response = await functions.getAll();
            setTarefas(response.items || []);
        } catch (error) {
            console.error('Erro ao carregar tarefas:', error);
            alert('Erro ao carregar tarefas');
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!formData.name.trim()) {
            alert('Por favor, insira um nome para a tarefa');
            return;
        }

        try {
            setLoading(true);
            await functions.create({
                name: formData.name,
                data: formData.data
            });
            
            setFormData({ name: '', data: '' });
            await carregarTarefas();
            
        } catch (error) {
            console.error('Erro ao criar tarefa:', error);
            alert(error || 'Erro ao criar tarefa');
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (tarefaNome) => {
        if (confirm(`Tem certeza que deseja excluir "${tarefaNome}"?`)) {
            try {
                setLoading(true);
                await functions.delete(tarefaNome);
                await carregarTarefas();
            } catch (error) {
                console.error('Erro ao excluir:', error);
                alert(error.detail || 'Erro ao excluir');
            } finally {
                setLoading(false);
            }
        }
    };

    return (
        <>
            <header>
                <h1>Notas 📆</h1>
            </header>
            
            <main>
                <form onSubmit={handleSubmit}>
                    <h2>Adicionar Nota</h2>
                    
                    <div>
                        <input 
                            type="text" 
                            name="name"
                            placeholder="Nome da nota"
                            value={formData.name}
                            onChange={handleInputChange}
                            required
                        />
                        
                        <input 
                            type="date" 
                            name="data"
                            value={formData.data}
                            onChange={handleInputChange}
                        />
                        
                        <button type="submit" disabled={loading}>
                            {loading ? 'Enviando...' : 'Adicionar Nota'}
                        </button>
                    </div>
                </form>

                <section>
                    <h2>Notas</h2>
                    
                    {loading ? (
                        <p>Carregando...</p>
                    ) : tarefas.length > 0 ? (
                        <div>
                            {tarefas.map((tarefa, index) => (
                                <div key={index}>
                                    <span>{tarefa.name}</span>
                                    <small>{tarefa.descricao}</small>
                                    <span>{tarefa.data}</span>
                                    <button 
                                    onClick={() => handleDelete(tarefa.name)}
                                    disabled={loading}
                                    >
                                    🗑️
                                    </button>
                                </div>
                            ))}
                        </div>
                    ) : (
                        <p>Não há notas cadastradas</p>
                    )}
                </section>
            </main>
        </>
    );
};

export default Home;